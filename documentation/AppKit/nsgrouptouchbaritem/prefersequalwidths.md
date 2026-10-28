# prefersEqualWidths

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that specifies that items should have equal widths when possible.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.13+

## Declaration

```swift
var prefersEqualWidths: Bool { get set }
```

```objc
@property BOOL prefersEqualWidths;
```

## Discussion

When [`true`](../../Swift/true.md), items in the [`groupTouchBar`](./grouptouchbar.md) are sized to have equal widths when possible.

The default value is [`false`](../../Swift/false.md).

## See Also

### Configuring item width
- [var preferredItemWidth: CGFloat](./preferreditemwidth.md)
  The preferred width for items in the group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgrouptouchbaritem/prefersequalwidths)*