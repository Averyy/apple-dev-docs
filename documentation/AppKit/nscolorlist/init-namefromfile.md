# init(name:fromFile:)

**Framework**: AppKit  
**Kind**: init

Initializes and returns a color list from the specified file, registering it under the specified name if it isn’t in use already.

**Availability**:
- macOS ?+

## Declaration

```swift
init?(name: NSColorList.Name, fromFile path: String?)
```

#### Discussion

Note that this method does not add the color list to [`availableColorLists`](nscolorlist/availablecolorlists.md) until the color list is saved into the user’s path with [`write(toFile:)`](nscolorlist/write(tofile:).md) with a value of `nil`.

## Parameters

- `name`: The name of the file for the color list (minus the   extension). Specify   if you don’t want a name.
- `path`: The full path to the file for the color list. A   path indicates the color list should be initialized with no colors.

## See Also

- [init(name: NSColorList.Name)](nscolorlist/init(name:).md)
  Initializes and returns a color list, registering it under the specified name if it isn’t in use already.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorlist/init(name:fromfile:))*