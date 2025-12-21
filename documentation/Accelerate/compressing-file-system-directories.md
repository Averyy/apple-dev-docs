# Compressing file system directories

**Framework**: Accelerate

Compress the contents of an entire directory and store the result on the file system.

#### Overview

In this article, you’ll learn how to use AppleArchive to compress the contents of an entire directory to a single archive file.

The code below compresses the contents of a directory name `src` using the [`Algorithm.lzfse`](https://developer.apple.com/documentation/Compression/Algorithm/lzfse) algorithm, and stores the result in a file named `directory.aar`.

##### Create the File Stream to Write the Compressed File

Use [`fileStream(path:mode:options:permissions:)`](https://developer.apple.com/documentation/AppleArchive/ArchiveByteStream/fileStream(path:mode:options:permissions:)) to create the file stream that writes the compressed file to the file system. In this case, use the [`writeOnly`](https://developer.apple.com/documentation/System/FileDescriptor/AccessMode/writeOnly) mode:

```swift
let archiveDestination = NSTemporaryDirectory() + "directory.aar"
let archiveFilePath = FilePath(archiveDestination)

guard let writeFileStream = ArchiveByteStream.fileStream(
        path: archiveFilePath,
        mode: .writeOnly,
        options: [ .create ],
        permissions: FilePermissions(rawValue: 0o644)) else {
    return
}
defer {
    try? writeFileStream.close()
}
```

##### Create the Compression Stream

Create the compression stream, and specify the compression algorithm as [`lzfse`](https://developer.apple.com/documentation/AppleArchive/ArchiveCompression/lzfse). Specify the file-writing stream as the stream that receives the compressed data:

```swift
guard let compressStream = ArchiveByteStream.compressionStream(
        using: .lzfse,
        writingTo: writeFileStream) else {
    return
}
defer {
    try? compressStream.close()
}
```

##### Create the Encoding Stream

Create the encoding stream. The encoding stream encodes its data as a byte stream, and sends the encoded data to the compression stream:

```swift
guard let encodeStream = ArchiveStream.encodeStream(writingTo: compressStream) else {
    return
}
defer {
    try? encodeStream.close()
}
```

##### Define the Header Keys

Create a field key set that defines the fields in the archive header:

```swift
guard let keySet = ArchiveHeader.FieldKeySet("TYP,PAT,LNK,DEV,DAT,UID,GID,MOD,FLG,MTM,BTM,CTM") else {
    return
}
```

For more information about three-letter keys, see [`init(_:)`](https://developer.apple.com/documentation/AppleArchive/ArchiveHeader/FieldKeySet/init(_:)).

##### Compress the Directory Contents

Use [`writeDirectoryContents(archiveFrom:path:keySet:selectUsing:flags:threadCount:)`](https://developer.apple.com/documentation/AppleArchive/ArchiveStream/writeDirectoryContents(archiveFrom:path:keySet:selectUsing:flags:threadCount:)) to write the directory contents to the encode stream. In turn, the encode stream writes to the compression stream and then, the compression stream writes to the file stream. Finally, the file stream writes the archive file to the file system:

```swift
let sourcePath = NSTemporaryDirectory() + "src/"
let source = FilePath(sourcePath)

do {
    try encodeStream.writeDirectoryContents(
        archiveFrom: source,
        keySet: keySet)
} catch {
    fatalError("Write directory contents failed.")
}
```

On return, `directory.aar` exists in [`NSTemporaryDirectory()`](https://developer.apple.com/documentation/Foundation/NSTemporaryDirectory()) and contains the compressed contents of `src/`.

## See Also

- [Compressing single files](compressing-single-files.md)
  Compress a single file and store the result on the file system.
- [Decompressing single files](decompressing-single-files.md)
  Recreate a single file from a compressed file.
- [Decompressing and extracting an archived directory](decompressing-and-extracting-an-archived-directory.md)
  Recreate an entire file system directory from an archive file.
- [Compressing and saving a string to the file system](compressing-and-saving-a-string-to-the-file-system.md)
  Compress the contents of a Unicode string and store the result on the file system.
- [Decompressing and parsing an archived string](decompressing-and-parsing-an-archived-string.md)
  Recreate a string from an archive file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/compressing-file-system-directories)*