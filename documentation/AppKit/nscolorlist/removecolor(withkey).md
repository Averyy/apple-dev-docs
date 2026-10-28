# removeColor(withKey:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Removes the color associated with the specified key from the color list.

**Availability**:
- macOS

## Declaration

```swift
func removeColor(withKey key: NSColor.Name)
```

```objc
- (void) removeColorWithKey:(NSColorName) key;
```

## Discussion

This method does nothing if the receiver doesn’t contain the key. This method posts [`didChangeNotification`](./didchangenotification.md) to the default notification center. It raises `NSColorListNotEditableException` if the receiver is not editable.

## Parameters

- `key`: The key for which to remove the color.

## See Also

### Managing Colors By Key
- [var allKeys: [NSColor.Name]](./allkeys.md)
  An array of the keys by which the color objects are stored in the color list.
- [func color(withKey: NSColor.Name) -> NSColor?](./color%28withkey%29.md)
  Returns the color object associated with the specified key.
- [func insertColor(NSColor, key: NSColor.Name, at: Int)](./insertcolor%28_,key,at%29.md)
  Inserts the specified color at the specified location in the color list.
- [func setColor(NSColor, forKey: NSColor.Name)](./setcolor%28_,forkey%29.md)
  Associates the specified color object with the specified key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorlist/removecolor(withkey:))*