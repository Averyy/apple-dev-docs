# tabStopType

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The text tab’s type of tab stop.

**Availability**:
- macOS 10.0+ - Deprecated in 27.0

> **Deprecated**: Use -alignment and -options.

## Declaration

```swift
var tabStopType: NSParagraphStyle.TextTabType { get }
```

```objc
@property (readonly) NSTextTabType tabStopType;
```

## Discussion

Possible values are listed in [`NSParagraphStyle.TextTabType`](../nsparagraphstyle/texttabtype.md).

## See Also

### Deprecated
- [convenience init(type: NSParagraphStyle.TextTabType, location: CGFloat)](./init%28type,location%29.md)
  Initializes a newly allocated text tab with the specified alignment and location.
- [NSParagraphStyle.TextTabType](../nsparagraphstyle/texttabtype.md)
  Constants that specify the type of tab stop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstexttab/tabstoptype)*