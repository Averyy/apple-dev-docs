# drawsBackground

**Framework**: AppKit  
**Kind**: property

A Boolean that controls whether the receiver draws its background.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var drawsBackground: Bool { get set }
```

#### Discussion

If `flag` is [`true`](https://developer.apple.com/documentation/swift/true), the receiver fills its background with the background color, if `flag` is [`false`](https://developer.apple.com/documentation/swift/false), it doesn’t.

## See Also

- [var backgroundColor: NSColor?](nstext/backgroundcolor.md)
  The receiver’s background color to a given color.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstext/drawsbackground)*