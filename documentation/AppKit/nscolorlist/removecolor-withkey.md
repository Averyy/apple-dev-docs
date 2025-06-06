# removeColor(withKey:)

**Framework**: AppKit  
**Kind**: method

Removes the color associated with the specified key from the color list.

**Availability**:
- macOS ?+

## Declaration

```swift
func removeColor(withKey key: NSColor.Name)
```

#### Discussion

This method does nothing if the receiver doesn’t contain the key. This method posts [`didChangeNotification`](nscolorlist/didchangenotification.md) to the default notification center. It raises `NSColorListNotEditableException` if the receiver is not editable.

## Parameters

- `key`: The key for which to remove the color.

## See Also

- [var allKeys: [NSColor.Name]](nscolorlist/allkeys.md)
  An array of the keys by which the color objects are stored in the color list.
- [func color(withKey: NSColor.Name) -> NSColor?](nscolorlist/color(withkey:).md)
  Returns the color object associated with the specified key.
- [func insertColor(NSColor, key: NSColor.Name, at: Int)](nscolorlist/insertcolor(_:key:at:).md)
  Inserts the specified color at the specified location in the color list.
- [func setColor(NSColor, forKey: NSColor.Name)](nscolorlist/setcolor(_:forkey:).md)
  Associates the specified color object with the specified key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorlist/removecolor(withkey:))*