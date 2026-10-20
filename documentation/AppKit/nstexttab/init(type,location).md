# init(type:location:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Initializes a newly allocated text tab with the specified alignment and location.

**Availability**:
- macOS 10.0+ - Deprecated in 27.0

## Declaration

```swift
convenience init(type: NSParagraphStyle.TextTabType, location loc: CGFloat)
```

```objc
- (instancetype) initWithType:(NSTextTabType) type location:(CGFloat) loc;
```

#### Discussion

The location is relative to the back margin, based on the line sweep direction of the paragraph. The value in the `type` parameter can be any of the values described in [`NSParagraphStyle.TextTabType`](../nsparagraphstyle/texttabtype.md).

## See Also

### Deprecated
- [var tabStopType: NSParagraphStyle.TextTabType](./tabstoptype.md)
  The text tab’s type of tab stop.
- [NSParagraphStyle.TextTabType](../nsparagraphstyle/texttabtype.md)
  Constants that specify the type of tab stop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstexttab/init(type:location:))*