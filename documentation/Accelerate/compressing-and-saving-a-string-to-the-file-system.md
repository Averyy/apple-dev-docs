# Compressing and saving a string to the file system

**Framework**: Accelerate  
**Role**: Article

Compress the contents of a Unicode string and store the result on the file system.

## Overview

In this article, you’ll learn how to use AppleArchive to compress a [`String`](../Swift/string.md) structure, and write the compressed data to a file in macOS.

The code below compresses a string using the [`Algorithm.lzfse`](../Compression/algorithm/lzfse.md) algorithm, and stores the result as `lorem.txt` in an AppleArchive file named `lorem.aar`. The code writes `lorem.aar` to the user’s `Downloads` directory.

### Create the source string

Create a string that contains the data the code compresses.

In a real-world app, you’ll most likely generate the string from a source such as user input. For this example, specify the string as a literal:

```swift
    static var loremString = """
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam fermentum vestibulum est. Cras rhoncus. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Sed quis tortor. Donec non ipsum. Mauris condimentum, odio nec porta tristique, ante neque malesuada massa, in dignissim eros velit at tellus. Donec et risus in ligula eleifend consectetur. Donec volutpat eleifend augue. Integer gravida sodales leo. Nunc vehicula neque ac erat. Vivamus non nisl. Fusce ac magna. Suspendisse euismod libero eget mauris.
    [...]
    """
```

### Specify the compressed file path

Create a [`FilePath`](../System/filepath.md) structure that specifies the file name and location of the AppleArchive file that stores the compressed data. You must add read and write file access to the Downloads folder in the Signing and Capabilities pane. To learn more about configuring the App Sandbox, see [App Sandbox](../Security/app-sandbox.md).

The following code creates a file path to `lorem.aar`:

```swift
let archiveFileName = "lorem.aar"

let archiveFilePath: FilePath = { 
    guard let downloadURL = FileManager.default.urls(for: .downloadsDirectory,
                                                     in: .userDomainMask).first,
          let archiveFilePath = FilePath(downloadURL.appendingPathComponent(archiveFileName)) else {
        fatalError("Unable to create archive file path.")
    }
    
    return archiveFilePath
}()
```

### Create the file stream to write the compressed File

Use `fileStream(path:mode:options:permissions:)` to create the file stream that writes the compressed file to the file system. In this case, use the [`writeOnly`](../System/filedescriptor/accessmode/writeonly.md) mode. Set the options as:

- **[`create`](../System/filedescriptor/openoptions/create.md)**: To specify that the byte stream creates the file if it doesn’t already exist.
- **[`truncate`](../System/filedescriptor/openoptions/truncate.md)**: To specify that if the file exists, the byte stream truncates it to zero bytes before it performs any operations.

```swift
guard let writeFileStream = ArchiveByteStream.fileStream(
        path: archiveFilePath,
        mode: .writeOnly,
        options: [ .create, .truncate ],
        permissions: FilePermissions(rawValue: 0o644)) else {
    return
}
defer {
    try? writeFileStream.close()
}
```

### Create the compression stream

Create the compression stream, and specify the compression algorithm as [`lzfse`](../AppleArchive/archivecompression/lzfse.md). Specify the file-writing stream as the stream that receives the compressed data:

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

### Create the encoding stream

Create the encoding stream. The encoding stream encodes its data as a byte stream, and sends the encoded data to the compression stream:

```swift
guard let encodeStream = ArchiveStream.encodeStream(writingTo: compressStream) else {
    return
}
defer {
    try? encodeStream.close()
}
```

### Define the archive header

Define the header for the archive file. The header contains three fields:

The `PAT` field contains the file path. Specify the unarchived file name for the `PAT` field:

```swift
let header = ArchiveHeader()
header.append(.string(key: ArchiveHeader.FieldKey("PAT"),
                      value: "lorem.txt"))
```

The `TYP` field contains the compressed file type. Specify [`regularFile`](../AppleArchive/archiveheader/entrytype-swift.struct/regularfile.md) for the `TYP` field:

```swift
header.append(.uint(key: ArchiveHeader.FieldKey("TYP"),
                    value:  UInt64(ArchiveHeader.EntryType.regularFile.rawValue)))
```

The `DAT` field contains the compressed file payload. Specify the size of the uncompressed data, in bytes, for the `DAT` field:

```swift
header.append(.blob(key: ArchiveHeader.FieldKey("DAT"),
                    size: UInt64(loremString.utf8.count)))
```

For more information about three-letter keys, see [`init(_:)`](../AppleArchive/archiveheader/fieldkeyset/init%28_%29.md).

Finally, write the header to the encode stream:

```swift
do {
    try encodeStream.writeHeader(header)
} catch {
    print("Failed to write header.")
}
```

### Write the string to the encode stream

Use [`writeBlob(key:from:)`](../AppleArchive/archivestreamprotocol/writeblob%28key,from%29.md) to write the contents of the string as a blob to the encode stream. In turn, the encode stream writes to the compression stream and then, the compression stream writes to the file stream. Finally, the file stream writes the archive file to the file system:

```swift
do {
    try loremString.withUTF8 { textPtr in
        
        let rawBufferPointer = UnsafeRawBufferPointer(textPtr)
        
        try encodeStream.writeBlob(key: ArchiveHeader.FieldKey("DAT"),
                                   from: rawBufferPointer)
    }
} catch {
    print("Failed to write blob.")
}
```

On return, `lorem.aar` exists as an AppleArchive file in the user’s `Downloads` directory and contains a single compressed text file, `lorem.txt`. The content of this text file is `loremString`.

## See Also

### Directories, Files, and Data Archives
- [Compressing single files](./compressing-single-files.md)
  Compress a single file and store the result on the file system.
- [Decompressing single files](./decompressing-single-files.md)
  Recreate a single file from a compressed file.
- [Compressing file system directories](./compressing-file-system-directories.md)
  Compress the contents of an entire directory and store the result on the file system.
- [Decompressing and extracting an archived directory](./decompressing-and-extracting-an-archived-directory.md)
  Recreate an entire file system directory from an archive file.
- [Decompressing and parsing an archived string](./decompressing-and-parsing-an-archived-string.md)
  Recreate a string from an archive file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/compressing-and-saving-a-string-to-the-file-system)*