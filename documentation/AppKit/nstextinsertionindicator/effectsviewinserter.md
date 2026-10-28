# effectsViewInserter

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

An optional closure the system calls during dictation.

**Availability**:
- macOS 14.0+

## Declaration

```swift
var effectsViewInserter: ((NSView) -> Void)? { get set }
```

```objc
@property (copy, nullable) void (^effectsViewInserter)(NSView *view);
```

## Mentions

- [Adopting the system text cursor in custom text views](../adopting-the-system-text-cursor-in-custom-text-views.md)

## Discussion

Use this property to add the view that displays the trailing glow to the view hierarchy. The system calls the closure when it needs to display the glow effect view.

During dictation the indicator displays a glow effect above the text view and below the insertion indicator. It’s the closure’s responsibility to add the glow effect view to the view hierarchy.

## See Also

### Configuring indicators
- [var color: NSColor!](./color.md)
  The color of this indicator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextinsertionindicator/effectsviewinserter)*