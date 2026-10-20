# color(withKey:)

**Framework**: AppKit  
**Kind**: method

Returns the color object associated with the specified key.

**Availability**:
- macOS ?+

## Declaration

```swift
func color(withKey key: NSColor.Name) -> NSColor?
```

#### Return Value

The color associated with the given key or `nil` if there is none.

## Parameters

- `key`: The key for which to retrieve the color.

## See Also

- [var allKeys: [NSColor.Name]](nscolorlist/allkeys.md)
  An array of the keys by which the color objects are stored in the color list.
- [func insertColor(NSColor, key: NSColor.Name, at: Int)](nscolorlist/insertcolor(_:key:at:).md)
  Inserts the specified color at the specified location in the color list.
- [func removeColor(withKey: NSColor.Name)](nscolorlist/removecolor(withkey:).md)
  Removes the color associated with the specified key from the color list.
- [func setColor(NSColor, forKey: NSColor.Name)](nscolorlist/setcolor(_:forkey:).md)
  Associates the specified color object with the specified key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorlist/color(withkey:))*