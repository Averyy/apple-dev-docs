# setColor(_:forKey:)

**Framework**: AppKit  
**Kind**: method

Associates the specified color object with the specified key.

**Availability**:
- macOS ?+

## Declaration

```swift
func setColor(_ color: NSColor, forKey key: NSColor.Name)
```

#### Discussion

If the list already contains `key`, this method sets the corresponding color to `color`; otherwise, it inserts `color` at the end of the list by invoking [`insertColor(_:key:at:)`](nscolorlist/insertcolor(_:key:at:).md).

## Parameters

- `color`: The color to associate with the given key.
- `key`: The key.

## See Also

- [var allKeys: [NSColor.Name]](nscolorlist/allkeys.md)
  An array of the keys by which the color objects are stored in the color list.
- [func color(withKey: NSColor.Name) -> NSColor?](nscolorlist/color(withkey:).md)
  Returns the color object associated with the specified key.
- [func insertColor(NSColor, key: NSColor.Name, at: Int)](nscolorlist/insertcolor(_:key:at:).md)
  Inserts the specified color at the specified location in the color list.
- [func removeColor(withKey: NSColor.Name)](nscolorlist/removecolor(withkey:).md)
  Removes the color associated with the specified key from the color list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorlist/setcolor(_:forkey:))*