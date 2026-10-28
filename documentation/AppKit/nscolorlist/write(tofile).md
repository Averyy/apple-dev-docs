# write(toFile:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Saves the color list to the file at the specified path.

**Availability**:
- macOS 10.0+ - Deprecated in 10.14

> **Deprecated**: Use [`write(to:)`](./write%28to%29.md) instead.

## Declaration

```swift
func write(toFile path: String?) -> Bool
```

```objc
- (BOOL) writeToFile:(NSString *) path;
```

## Return Value

[`true`](../../Swift/true.md) upon success and [`false`](../../Swift/false.md) if the method fails to write the file.

## Parameters

- `path`: The path at which to save the color list. If `path` is a directory, the receiver is saved in a file named listname`.clr` in that directory (where listname is the name with which the receiver was initialized).

  If `path` includes a filename, this method saves the file under that name. If `path` is `nil`,  the file is saved as listname`.clr` in the user’s private colorlists directory.

## See Also

### Writing and Removing Color List Files
- [func write(to: URL?) throws](./write%28to%29.md)
  Saves the color list to the file at the specified URL.
- [func removeFile()](./removefile%28%29.md)
  Removes the file from which the list was created, if the file is in a standard search path and owned by the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorlist/write(tofile:))*