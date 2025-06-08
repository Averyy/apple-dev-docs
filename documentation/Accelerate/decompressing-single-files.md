# Decompressing single files

**Framework**: Accelerate

Recreate a single file from a compressed file.

#### Overview

In this article, you’ll learn how to use AppleArchive to decompress a previously compressed file, and write the decompressed data to a file.

The code below decompresses the file generated using the steps explained in [`Compressing single files`](compressing-single-files.md).

##### Create the File Stream to Read the Source Archive

The [`ArchiveByteStream`](https://developer.apple.com/documentation/AppleArchive/ArchiveByteStream) class provides static factory methods that create streams for different functions. In this case, use [`fileStream(path:mode:options:permissions:)`](https://developer.apple.com/documentation/AppleArchive/ArchiveByteStream/fileStream(path:mode:options:permissions:)) to create a byte stream that reads the source file:

```swift
let archiveFilePath = FilePath(NSTemporaryDirectory() + "myFile.pdf.lzfse")

guard let readFileStream = ArchiveByteStream.fileStream(
        path: archiveFilePath,
        mode: .readOnly,
        options: [ ],
        permissions: FilePermissions(rawValue: 0o644)) else {
    return
}
defer {
    try? readFileStream.close()
}
```

##### Create the File Stream to Write the Decompressed File

You also use [`fileStream(path:mode:options:permissions:)`](https://developer.apple.com/documentation/AppleArchive/ArchiveByteStream/fileStream(path:mode:options:permissions:)) to create the file stream that writes the decompressed file to the file system. In this case, use the [`writeOnly`](https://developer.apple.com/documentation/System/FileDescriptor/AccessMode/writeOnly) mode:

```swift
let destinationFilePath = FilePath(NSTemporaryDirectory() + "myFile_decompressed.pdf")

guard let writeFileStream = ArchiveByteStream.fileStream(
        path: destinationFilePath,
        mode: .writeOnly,
        options: [ .create ],
        permissions: FilePermissions(rawValue: 0o644)) else {
    return
}
defer {
    try? writeFileStream.close()
}
```

##### Create the Decompression Stream

Create the decompression stream. Specify the file-reading stream as the input stream that provides the compressed data:

```swift
guard let decompressStream = ArchiveByteStream.decompressionStream(readingFrom: readFileStream) else {
    print("unable to create compress stream")
    return
}
defer {
    try? decompressStream.close()
}
```

##### Decompress the Source Archive

Finally, call [`process(readingFrom:writingTo:)`](https://developer.apple.com/documentation/AppleArchive/ArchiveByteStream/process(readingFrom:writingTo:)) to write the output of the decompression stream to the file-writing stream:

```swift
do {
    _ = try ArchiveByteStream.process(readingFrom: decompressStream,
                                      writingTo: writeFileStream)
} catch {
    print("Handle `ArchiveByteStream.process` failed.")
}
```

On return, `myFile_decompressed.pdf` exists in [`NSTemporaryDirectory()`](https://developer.apple.com/documentation/foundation/1409211-nstemporarydirectory) and contains the decompressed contents of `myFile.pdf.lzfse`.

## See Also

- [Compressing single files](compressing-single-files.md)
  Compress a single file and store the result on the file system.
- [Compressing file system directories](compressing-file-system-directories.md)
  Compress the contents of an entire directory and store the result on the file system.
- [Decompressing and extracting an archived directory](decompressing-and-extracting-an-archived-directory.md)
  Recreate an entire file system directory from an archive file.
- [Compressing and saving a string to the file system](compressing-and-saving-a-string-to-the-file-system.md)
  Compress the contents of a Unicode string and store the result on the file system.
- [Decompressing and Parsing an Archived String](decompressing-and-parsing-an-archived-string.md)
  Recreate a string from an archive file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/decompressing-single-files)*