# showsAdditionalContentIndicators

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that specifies whether the scrubber should display the existence of additional items beyond the leading and trailing edges.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
var showsAdditionalContentIndicators: Bool { get set }
```

```objc
@property BOOL showsAdditionalContentIndicators;
```

## Discussion

When [`true`](../../Swift/true.md), the scrubber uses a fade effect to indicate that there is additional content the user can scroll to. The default value is [`false`](../../Swift/false.md).

## See Also

### Configuring the scrubber’s appearance
- [var backgroundColor: NSColor?](./backgroundcolor.md)
  The color displayed behind the scrubber content.
- [var backgroundView: NSView?](./backgroundview.md)
  A view that is displayed behind the scrubber content.
- [var showsArrowButtons: Bool](./showsarrowbuttons.md)
  A Boolean value that specifies whether arrow buttons should be displayed at the leading and trailing edges of the scrubber.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrubber/showsadditionalcontentindicators)*