# init(named:)

**Framework**: AppKit  
**Kind**: init

Searches the available color lists array and returns the color list with the specified name.

**Availability**:
- macOS ?+

## Declaration

```swift
init?(named name: NSColorList.Name)
```

#### Return Value

The color list with the specified name or `nil` if no such color list exists.

## Parameters

- `name`: The name of the color list to retrieve. This name must not include the “ ” suffix.

## See Also

- [var name: NSColorList.Name?](nscolorlist/name-swift.property.md)
  The name of the color list.
- [class var availableColorLists: [NSColorList]](nscolorlist/availablecolorlists.md)
  Returns an array of all color lists found in the standard color list directories.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorlist/init(named:))*