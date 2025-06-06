# write(toFile:)

**Framework**: AppKit  
**Kind**: method

Saves the color list to the file at the specified path.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func write(toFile path: String?) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) upon success and [`false`](https://developer.apple.com/documentation/swift/false) if the method fails to write the file.

## Parameters

- `path`: If   includes a filename, this method saves the file under that name. If   is  ,  the file is saved as listname  in the user’s private colorlists directory.

## See Also

- [func write(to: URL?) throws](nscolorlist/write(to:).md)
  Saves the color list to the file at the specified URL.
- [func removeFile()](nscolorlist/removefile.md)
  Removes the file from which the list was created, if the file is in a standard search path and owned by the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorlist/write(tofile:))*