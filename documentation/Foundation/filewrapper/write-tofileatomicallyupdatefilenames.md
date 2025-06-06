# write(toFile:atomically:updateFilenames:)

**Framework**: Foundation  
**Kind**: method

Writes a file wrapper’s contents to a given file-system node.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func write(toFile path: String, atomically atomicFlag: Bool, updateFilenames updateFilenamesFlag: Bool) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) when the write operation is successful, [`false`](https://developer.apple.com/documentation/swift/false) otherwise.

#### Discussion

Beginning with OS X v10.6, the preferred method of referring to files is with a `file://` URL. Therefore, this method has been deprecated in favor of [`write(to:options:originalContentsURL:)`](filewrapper/write(to:options:originalcontentsurl:).md).

## Parameters

- `path`: Pathname of the file-system node to which the receiver’s contents are written.
- `atomicFlag`:  to overwrite an existing file and ignore incomplete writes.
- `updateFilenamesFlag`:  to specify that the receiver’s filenames not be updated. Use this in Save To operations.

## See Also

- [var filename: String?](filewrapper/filename.md)
  The filename of the file wrapper object
- [func write(to: URL, options: FileWrapper.WritingOptions, originalContentsURL: URL?) throws](filewrapper/write(to:options:originalcontentsurl:).md)
  Recursively writes the entire contents of a file wrapper to a given file-system URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filewrapper/write(tofile:atomically:updatefilenames:))*