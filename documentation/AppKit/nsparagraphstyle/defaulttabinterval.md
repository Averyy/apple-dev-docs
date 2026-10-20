# defaultTabInterval

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The documentwide default tab interval.

**Availability**:
- macOS 10.0+

## Declaration

```swift
var defaultTabInterval: CGFloat { get }
```

```objc
@property (readonly) CGFloat defaultTabInterval;
```

#### Discussion

This property represents the default tab interval in points. Tabs after the last specified in [`tabStops`](./tabstops.md) are placed at integer multiples of this distance (if positive). Default value is 0.0.

## See Also

### Accessing tab information
- [var tabStops: [NSTextTab]](./tabstops.md)
  The text tab objects that represent the paragraph’s tab stops.
- [NSParagraphStyle.TextTabType](./texttabtype.md)
  Constants that specify the type of tab stop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsparagraphstyle/defaulttabinterval)*