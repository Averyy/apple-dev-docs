# visibleCharacterRanges

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

An array of visible character ranges.

**Availability**:
- macOS

## Declaration

```swift
optional var visibleCharacterRanges: [NSValue] { get }
```

```objc
@property (copy, readonly) NSArray<NSValue *> * visibleCharacterRanges;
```

#### Discussion

The text finder uses this property’s value to determine which ranges it should search to show all of the incremental matches that are currently visible.

If this property is not implemented, then the incremental matches cannot be shown.

The array contains `NSValue` objects that wrap `NSRect` structures.

## See Also

### Determining and Displaying Text Locations
- [func contentView(at: Int, effectiveCharacterRange: NSRangePointer) -> NSView](./contentview%28at,effectivecharacterrange%29.md)
  Returns the view the context is displayed in.
- [func rects(forCharacterRange: NSRange) -> [NSValue]?](./rects%28forcharacterrange%29.md)
  An array containing the located text in the content view’s coordinate system.
- [func scrollRangeToVisible(NSRange)](./scrollrangetovisible%28_%29.md)
  Scrolls the specified range such that it is visible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextfinderclient/visiblecharacterranges)*