# allKeys

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

An array of the keys by which the color objects are stored in the color list.

**Availability**:
- macOS

## Declaration

```swift
var allKeys: [NSColor.Name] { get }
```

```objc
@property (copy, readonly) NSArray<NSString *> * allKeys;
```

## See Also

### Managing Colors By Key
- [func color(withKey: NSColor.Name) -> NSColor?](./color%28withkey%29.md)
  Returns the color object associated with the specified key.
- [func insertColor(NSColor, key: NSColor.Name, at: Int)](./insertcolor%28_,key,at%29.md)
  Inserts the specified color at the specified location in the color list.
- [func removeColor(withKey: NSColor.Name)](./removecolor%28withkey%29.md)
  Removes the color associated with the specified key from the color list.
- [func setColor(NSColor, forKey: NSColor.Name)](./setcolor%28_,forkey%29.md)
  Associates the specified color object with the specified key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorlist/allkeys)*