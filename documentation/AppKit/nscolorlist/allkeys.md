# allKeys

**Framework**: AppKit  
**Kind**: property

An array of the keys by which the color objects are stored in the color list.

**Availability**:
- macOS ?+

## Declaration

```swift
var allKeys: [NSColor.Name] { get }
```

## See Also

- [func color(withKey: NSColor.Name) -> NSColor?](nscolorlist/color(withkey:).md)
  Returns the color object associated with the specified key.
- [func insertColor(NSColor, key: NSColor.Name, at: Int)](nscolorlist/insertcolor(_:key:at:).md)
  Inserts the specified color at the specified location in the color list.
- [func removeColor(withKey: NSColor.Name)](nscolorlist/removecolor(withkey:).md)
  Removes the color associated with the specified key from the color list.
- [func setColor(NSColor, forKey: NSColor.Name)](nscolorlist/setcolor(_:forkey:).md)
  Associates the specified color object with the specified key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorlist/allkeys)*