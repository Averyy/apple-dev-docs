# preferredItemWidth

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The preferred width for items in the group.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.13+

## Declaration

```swift
var preferredItemWidth: CGFloat { get set }
```

```objc
@property CGFloat preferredItemWidth;
```

#### Discussion

This width applies when [`prefersEqualWidths`](./prefersequalwidths.md) is [`true`](../../Swift/true.md).

This is the width that items are set to if there is enough room, and if the items don’t clip.

This value is ignored if it is negative. The default value is `-1`.

## See Also

### Configuring item width
- [var prefersEqualWidths: Bool](./prefersequalwidths.md)
  A Boolean value that specifies that items should have equal widths when possible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgrouptouchbaritem/preferreditemwidth)*