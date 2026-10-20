# horizontallyCentered

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

An `NSNumber` object containing a Boolean value that specifies whether to horizontally center pages.

**Availability**:
- macOS

## Declaration

```swift
static let horizontallyCentered: NSPrintInfo.AttributeKey
```

```c
extern NSPrintInfoAttributeKey const NSPrintHorizontallyCentered;
```

#### Discussion

If [`true`](../../../Swift/true.md), pages are centered horizontally.

## See Also

### Pagination Attributes
- [static let leftMargin: NSPrintInfo.AttributeKey](./leftmargin.md)
  `NSNumber`, containing a floating-point value that specifies the left margin, in points.
- [static let rightMargin: NSPrintInfo.AttributeKey](./rightmargin.md)
  `NSNumber`, containing a floating-point value that specifies the right margin, in points.
- [static let topMargin: NSPrintInfo.AttributeKey](./topmargin.md)
  `NSNumber`, containing a floating-point value that specifies the top margin, in points.
- [static let bottomMargin: NSPrintInfo.AttributeKey](./bottommargin.md)
  `NSNumber`, containing a floating-point value that specifies the bottom margin, in points.
- [static let verticallyCentered: NSPrintInfo.AttributeKey](./verticallycentered.md)
  An `NSNumber` object containing a Boolean value that specifies whether to vertically center pages.
- [static let horizontalPagination: NSPrintInfo.AttributeKey](./horizontalpagination.md)
  `NSNumber`, containing a `NSPrintingPaginationMode` value.
- [static let verticalPagination: NSPrintInfo.AttributeKey](./verticalpagination.md)
  `NSNumber`, containing a `NSPrintingPaginationMode` value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprintinfo/attributekey/horizontallycentered)*