# write(toFile:atomically:updateFilenames:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Writes a file wrapper’s contents to a given file-system node.

**Availability**:
- macOS 10.0+ - Deprecated in 10.10

> **Deprecated**: Use [`write(to:options:originalContentsURL:)`](./write%28to,options,originalcontentsurl%29.md) instead.

## Declaration

```swift
func write(toFile path: String, atomically atomicFlag: Bool, updateFilenames updateFilenamesFlag: Bool) -> Bool
```

```objc
- (BOOL) writeToFile:(NSString *) path atomically:(BOOL) atomicFlag updateFilenames:(BOOL) updateFilenamesFlag;
```

## Return Value

[`true`](../../Swift/true.md) when the write operation is successful, [`false`](../../Swift/false.md) otherwise.

## Discussion

Beginning with OS X v10.6, the preferred method of referring to files is with a `file://` URL. Therefore, this method has been deprecated in favor of [`write(to:options:originalContentsURL:)`](./write%28to,options,originalcontentsurl%29.md).

## Parameters

- `path`: Pathname of the file-system node to which the receiver’s contents are written.
- `atomicFlag`: [`true`](../../Swift/true.md) to write the file safely so that:

  - An existing file is not overwritten
  - The method fails if the file cannot be written in its entirety

  [`false`](../../Swift/false.md) to overwrite an existing file and ignore incomplete writes.
- `updateFilenamesFlag`: [`true`](../../Swift/true.md) to update the receiver’s filenames (its filename and—for directory file wrappers—the filenames of its sub–file wrappers) be changed to the filenames of the corresponding nodes in the file system, after a successful write operation. Use this in Save or Save As operations.

  [`false`](../../Swift/false.md) to specify that the receiver’s filenames not be updated. Use this in Save To operations.

## See Also

### Related Documentation
- [var filename: String?](./filename.md)
  The filename of the file wrapper object
### Writing Files
- [func write(to: URL, options: FileWrapper.WritingOptions, originalContentsURL: URL?) throws](./write%28to,options,originalcontentsurl%29.md)
  Recursively writes the entire contents of a file wrapper to a given file-system URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filewrapper/write(tofile:atomically:updatefilenames:))*