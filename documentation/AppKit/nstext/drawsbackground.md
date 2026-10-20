# drawsBackground

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean that controls whether the receiver draws its background.

**Availability**:
- macOS

## Declaration

```swift
var drawsBackground: Bool { get set }
```

```objc
@property BOOL drawsBackground;
```

#### Discussion

If `flag` is [`true`](../../Swift/true.md), the receiver fills its background with the background color, if `flag` is [`false`](../../Swift/false.md), it doesn’t.

## See Also

### Setting graphics attributes
- [var backgroundColor: NSColor?](./backgroundcolor.md)
  The receiver’s background color to a given color.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstext/drawsbackground)*