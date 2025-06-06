# insertColor(_:key:at:)

**Framework**: AppKit  
**Kind**: method

Inserts the specified color at the specified location in the color list.

**Availability**:
- macOS ?+

## Declaration

```swift
func insertColor(_ color: NSColor, key: NSColor.Name, at loc: Int)
```

#### Discussion

If the list already contains a color with the same key at a different location, it’s removed from the old location. This method posts [`didChangeNotification`](nscolorlist/didchangenotification.md) to the default notification center. It raises `NSColorListNotEditableException` if the color list isn’t editable.

## Parameters

- `color`: The color to add to the color list.
- `key`: The key with which to associate the color.
- `loc`: The location in the color list at which to place the specified color. Locations are numbered starting with 0.

## See Also

- [var allKeys: [NSColor.Name]](nscolorlist/allkeys.md)
  An array of the keys by which the color objects are stored in the color list.
- [func color(withKey: NSColor.Name) -> NSColor?](nscolorlist/color(withkey:).md)
  Returns the color object associated with the specified key.
- [func removeColor(withKey: NSColor.Name)](nscolorlist/removecolor(withkey:).md)
  Removes the color associated with the specified key from the color list.
- [func setColor(NSColor, forKey: NSColor.Name)](nscolorlist/setcolor(_:forkey:).md)
  Associates the specified color object with the specified key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorlist/insertcolor(_:key:at:))*