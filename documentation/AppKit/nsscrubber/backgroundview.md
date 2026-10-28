# backgroundView

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A view that is displayed behind the scrubber content.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
var backgroundView: NSView? { get set }
```

```objc
@property (strong, nullable) NSView * backgroundView;
```

## Discussion

The scrubber manages the layout of the background view to match the size of the content area. If this property is non-`nil`, the value of the [`backgroundColor`](../nspathcontrol/backgroundcolor.md) property is ignored.

The default value is `nil`.

## See Also

### Configuring the scrubber’s appearance
- [var backgroundColor: NSColor?](./backgroundcolor.md)
  The color displayed behind the scrubber content.
- [var showsAdditionalContentIndicators: Bool](./showsadditionalcontentindicators.md)
  A Boolean value that specifies whether the scrubber should display the existence of additional items beyond the leading and trailing edges.
- [var showsArrowButtons: Bool](./showsarrowbuttons.md)
  A Boolean value that specifies whether arrow buttons should be displayed at the leading and trailing edges of the scrubber.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrubber/backgroundview)*