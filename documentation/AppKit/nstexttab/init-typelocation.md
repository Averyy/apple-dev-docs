# init(type:location:)

**Framework**: AppKit  
**Kind**: init

Initializes a newly allocated text tab with the specified alignment and location.

**Availability**:
- macOS ?+

## Declaration

```swift
convenience init(type: NSParagraphStyle.TextTabType, location loc: CGFloat)
```

#### Discussion

The location is relative to the back margin, based on the line sweep direction of the paragraph. The value in the `type` parameter can be any of the values described in [`NSParagraphStyle.TextTabType`](nsparagraphstyle/texttabtype.md).

## See Also

- [var tabStopType: NSParagraphStyle.TextTabType](nstexttab/tabstoptype.md)
  The text tab’s type of tab stop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstexttab/init(type:location:))*