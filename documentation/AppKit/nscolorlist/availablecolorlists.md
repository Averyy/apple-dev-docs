# availableColorLists

**Framework**: AppKit  
**Kind**: property

Returns an array of all color lists found in the standard color list directories.

**Availability**:
- macOS ?+

## Declaration

```swift
class var availableColorLists: [NSColorList] { get }
```

#### Return Value

An array of `NSColorList` objects representing all of the color lists found in the standard color list directories, including color catalogs (lists of colors identified only by name). Color lists created at runtime aren’t included in this list unless they’re saved into one of the standard color list directories.

## See Also

- [init?(named: NSColorList.Name)](nscolorlist/init(named:).md)
  Searches the available color lists array and returns the color list with the specified name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorlist/availablecolorlists)*