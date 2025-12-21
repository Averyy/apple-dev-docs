# showsAdditionalContentIndicators

**Framework**: AppKit  
**Kind**: property

A Boolean value that specifies whether the scrubber should display the existence of additional items beyond the leading and trailing edges.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
@MainActor
var showsAdditionalContentIndicators: Bool { get set }
```

#### Discussion

When [`true`](https://developer.apple.com/documentation/Swift/true), the scrubber uses a fade effect to indicate that there is additional content the user can scroll to. The default value is [`false`](https://developer.apple.com/documentation/Swift/false).

## See Also

- [var backgroundColor: NSColor?](nsscrubber/backgroundcolor.md)
  The color displayed behind the scrubber content.
- [var backgroundView: NSView?](nsscrubber/backgroundview.md)
  A view that is displayed behind the scrubber content.
- [var showsArrowButtons: Bool](nsscrubber/showsarrowbuttons.md)
  A Boolean value that specifies whether arrow buttons should be displayed at the leading and trailing edges of the scrubber.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrubber/showsadditionalcontentindicators)*