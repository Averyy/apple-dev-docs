# defaultTabInterval

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A number used as the document’s default tab spacing.

**Availability**:
- macOS 10.0+

## Declaration

```swift
var defaultTabInterval: CGFloat { get set }
```

```objc
@property CGFloat defaultTabInterval;
```

## Discussion

This property represents the default tab interval in points. The system places tabs after the last specified in [tabStops](https://developer.apple.com/library/archive/#id(tabStops)) at integer multiples of this distance (if positive). Default value is `0.0`.

## See Also

### Specifying tab information
- [func addTabStop(NSTextTab)](./addtabstop%28_%29.md)
  Adds the specified tab stop to the paragraph.
- [func removeTabStop(NSTextTab)](./removetabstop%28_%29.md)
  Removes the first text tab with a location and type equal to the specified tab stop.
- [var tabStops: [NSTextTab]!](./tabstops.md)
  The text tab objects that represent the paragraph’s tab stops.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmutableparagraphstyle/defaulttabinterval)*