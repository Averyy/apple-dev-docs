# backgroundColor

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The color displayed behind the scrubber content.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
@NSCopying
var backgroundColor: NSColor? { get set }
```

```objc
@property (copy, nullable) NSColor * backgroundColor;
```

## Discussion

The value of this property is ignored if the value of the [`backgroundView`](./backgroundview.md) property is non-`nil`. The default value is `nil`.

## See Also

### Configuring the scrubber’s appearance
- [var backgroundView: NSView?](./backgroundview.md)
  A view that is displayed behind the scrubber content.
- [var showsAdditionalContentIndicators: Bool](./showsadditionalcontentindicators.md)
  A Boolean value that specifies whether the scrubber should display the existence of additional items beyond the leading and trailing edges.
- [var showsArrowButtons: Bool](./showsarrowbuttons.md)
  A Boolean value that specifies whether arrow buttons should be displayed at the leading and trailing edges of the scrubber.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrubber/backgroundcolor)*