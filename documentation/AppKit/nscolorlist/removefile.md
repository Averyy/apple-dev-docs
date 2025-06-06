# removeFile()

**Framework**: AppKit  
**Kind**: method

Removes the file from which the list was created, if the file is in a standard search path and owned by the user.

**Availability**:
- macOS ?+

## Declaration

```swift
func removeFile()
```

#### Discussion

In addition to removing the file, this method removes the color list from the contents of the [`availableColorLists`](nscolorlist/availablecolorlists.md) property. If there are no outstanding references to the color list, this method might also deallocate the object.

## See Also

- [func write(to: URL?) throws](nscolorlist/write(to:).md)
  Saves the color list to the file at the specified URL.
- [func write(toFile: String?) -> Bool](nscolorlist/write(tofile:).md)
  Saves the color list to the file at the specified path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorlist/removefile())*