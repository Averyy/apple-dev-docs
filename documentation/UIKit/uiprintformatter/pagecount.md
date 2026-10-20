# pageCount

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The number of pages to print.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var pageCount: Int { get }
```

```objc
@property (nonatomic, readonly) NSInteger pageCount;
```

#### Discussion

`UIPrintFormatter` calculates this value based on the layout metrics and content.

## See Also

### Managing pagination
- [var startPage: Int](./startpage.md)
  The index of the first page that the print formatter lays out.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiprintformatter/pagecount)*