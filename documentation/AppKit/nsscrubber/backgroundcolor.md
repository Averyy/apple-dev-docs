# backgroundColor

**Framework**: AppKit  
**Kind**: property

The color displayed behind the scrubber content.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
@NSCopying
@MainActor var backgroundColor: NSColor? { get set }
```

#### Discussion

The value of this property is ignored if the value of the [`backgroundView`](nsscrubber/backgroundview.md) property is non-`nil`. The default value is `nil`.

## See Also

- [var backgroundView: NSView?](nsscrubber/backgroundview.md)
  A view that is displayed behind the scrubber content.
- [var showsAdditionalContentIndicators: Bool](nsscrubber/showsadditionalcontentindicators.md)
  A Boolean value that specifies whether the scrubber should display the existence of additional items beyond the leading and trailing edges.
- [var showsArrowButtons: Bool](nsscrubber/showsarrowbuttons.md)
  A Boolean value that specifies whether arrow buttons should be displayed at the leading and trailing edges of the scrubber.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrubber/backgroundcolor)*