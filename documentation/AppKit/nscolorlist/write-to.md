# write(to:)

**Framework**: AppKit  
**Kind**: method

Saves the color list to the file at the specified URL.

**Availability**:
- macOS 10.11+

## Declaration

```swift
func write(to url: URL?) throws
```

#### Discussion

If `url` represents a directory, this method saves the color list in that directory in a file with the name `.clr`, where  is the value of the [`name`](nscolorlist/name-swift.property.md) property. If `url` represents a file, this method saves the color list using the name you provided.

## Parameters

- `url`: The URL at which to store the color list. The URL must specify either a directory or file in the file system. Specify   to save the color list to the user’s   directory.

## See Also

- [func removeFile()](nscolorlist/removefile.md)
  Removes the file from which the list was created, if the file is in a standard search path and owned by the user.
- [func write(toFile: String?) -> Bool](nscolorlist/write(tofile:).md)
  Saves the color list to the file at the specified path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorlist/write(to:))*