# setColor(_:forKey:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Associates the specified color object with the specified key.

**Availability**:
- macOS

## Declaration

```swift
func setColor(_ color: NSColor, forKey key: NSColor.Name)
```

```objc
- (void) setColor:(NSColor *) color forKey:(NSColorName) key;
```

#### Discussion

If the list already contains `key`, this method sets the corresponding color to `color`; otherwise, it inserts `color` at the end of the list by invoking [`insertColor(_:key:at:)`](./insertcolor%28_,key,at%29.md).

## Parameters

- `color`: The color to associate with the given key.
- `key`: The key.

## See Also

### Managing Colors By Key
- [var allKeys: [NSColor.Name]](./allkeys.md)
  An array of the keys by which the color objects are stored in the color list.
- [func color(withKey: NSColor.Name) -> NSColor?](./color%28withkey%29.md)
  Returns the color object associated with the specified key.
- [func insertColor(NSColor, key: NSColor.Name, at: Int)](./insertcolor%28_,key,at%29.md)
  Inserts the specified color at the specified location in the color list.
- [func removeColor(withKey: NSColor.Name)](./removecolor%28withkey%29.md)
  Removes the color associated with the specified key from the color list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorlist/setcolor(_:forkey:))*