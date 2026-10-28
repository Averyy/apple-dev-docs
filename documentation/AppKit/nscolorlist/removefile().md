# removeFile()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Removes the file from which the list was created, if the file is in a standard search path and owned by the user.

**Availability**:
- macOS

## Declaration

```swift
func removeFile()
```

```objc
- (void) removeFile;
```

## Discussion

In addition to removing the file, this method removes the color list from the contents of the [`availableColorLists`](./availablecolorlists.md) property. If there are no outstanding references to the color list, this method might also deallocate the object.

## See Also

### Writing and Removing Color List Files
- [func write(to: URL?) throws](./write%28to%29.md)
  Saves the color list to the file at the specified URL.
- [func write(toFile: String?) -> Bool](./write%28tofile%29.md)
  Saves the color list to the file at the specified path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorlist/removefile())*