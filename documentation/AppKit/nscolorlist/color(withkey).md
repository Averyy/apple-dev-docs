# color(withKey:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the color object associated with the specified key.

**Availability**:
- macOS

## Declaration

```swift
func color(withKey key: NSColor.Name) -> NSColor?
```

```objc
- (NSColor *) colorWithKey:(NSColorName) key;
```

## Return Value

The color associated with the given key or `nil` if there is none.

## Parameters

- `key`: The key for which to retrieve the color.

## See Also

### Managing Colors By Key
- [var allKeys: [NSColor.Name]](./allkeys.md)
  An array of the keys by which the color objects are stored in the color list.
- [func insertColor(NSColor, key: NSColor.Name, at: Int)](./insertcolor%28_,key,at%29.md)
  Inserts the specified color at the specified location in the color list.
- [func removeColor(withKey: NSColor.Name)](./removecolor%28withkey%29.md)
  Removes the color associated with the specified key from the color list.
- [func setColor(NSColor, forKey: NSColor.Name)](./setcolor%28_,forkey%29.md)
  Associates the specified color object with the specified key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorlist/color(withkey:))*