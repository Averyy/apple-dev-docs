# Decompressing and extracting an archived directory

**Framework**: Accelerate  
**Role**: Article

Recreate an entire file system directory from an archive file.

## Overview

In this article, you’ll learn how to use AppleArchive to decompress and extract a previously compressed file system directory.

The code below decompresses the file generated using the steps explained in [Compressing file system directories](./compressing-file-system-directories.md) and writes the files to a directory named `dest`.

### Create the file stream to read the source archive

The [`ArchiveByteStream`](../AppleArchive/archivebytestream.md) class provides static factory methods that create streams for different functions. In this case, use [`fileStream(path:mode:options:permissions:)`](../AppleArchive/archivebytestream/filestream%28path,mode,options,permissions%29.md) to create a byte stream that reads the source file:

```swift
let archiveFilePath = FilePath(NSTemporaryDirectory() + "directory.aar")

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

### Create the decompression stream

Create the decompression stream. Specify the file-reading stream as the input stream that provides the compressed data:

```swift
guard let decompressStream = ArchiveByteStream.decompressionStream(readingFrom: readFileStream) else {
    return
}
defer {
    try? decompressStream.close()
}
```

### Create the decoding stream

Create a decoding stream that provides archive elements from the raw, decompressed data:

```swift
guard let decodeStream = ArchiveStream.decodeStream(readingFrom: decompressStream) else {
    print("unable to create decode stream")
    return
}
defer {
    try? decodeStream.close()
}
```

### Specify the destination

Specify a destination path for the decompressed directory contents. The following code checks that the destination directory exists and creates the destination if neccessary:

```swift
let decompressPath = NSTemporaryDirectory() + "dest/"

if !FileManager.default.fileExists(atPath: decompressPath) {
    do {
        try FileManager.default.createDirectory(atPath: decompressPath,
                                                withIntermediateDirectories: false)
    } catch {
        fatalError("Unable to create destination directory.")
    }
}

let decompressDestination = FilePath(decompressPath)
```

### Create the extract stream

Create an extract stream that receives archive elements, and extracts to the specified directory:

```swift
guard let extractStream = ArchiveStream.extractStream(extractingTo: decompressDestination,
                                                      flags: [ .ignoreOperationNotPermitted ]) else {
    return
}
defer {
    try? extractStream.close()
}
```

### Decompress and extract the archived directory

Finally, call [`process(readingFrom:writingTo:)`](../AppleArchive/archivebytestream/process%28readingfrom,writingto%29.md) to write the output of the decode stream to the extract stream. In turn, the extract stream extracts each archive element to the decompression destination:

```swift
do {
    _ = try ArchiveStream.process(readingFrom: decodeStream,
                                  writingTo: extractStream)
} catch {
    print("process failed")
}
```

On return, the operation recreates the contents of the directory previously archived in `directory.aar` in [`NSTemporaryDirectory()`](../Foundation/nstemporarydirectory%28%29.md) `+ “dest/”.`

## See Also

### Directories, Files, and Data Archives
- [Compressing single files](./compressing-single-files.md)
  Compress a single file and store the result on the file system.
- [Decompressing single files](./decompressing-single-files.md)
  Recreate a single file from a compressed file.
- [Compressing file system directories](./compressing-file-system-directories.md)
  Compress the contents of an entire directory and store the result on the file system.
- [Compressing and saving a string to the file system](./compressing-and-saving-a-string-to-the-file-system.md)
  Compress the contents of a Unicode string and store the result on the file system.
- [Decompressing and parsing an archived string](./decompressing-and-parsing-an-archived-string.md)
  Recreate a string from an archive file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/decompressing-and-extracting-an-archived-directory)*