# printableRect

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The area in which printing can occur.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var printableRect: CGRect { get }
```

```objc
@property (nonatomic, readonly) CGRect printableRect;
```

## Discussion

The value of this property is a rectangle that defines the area in which the printer can print content. Sometimes this is referred to as the imageable area of the paper.

## See Also

### Related Documentation
- [var printPaper: UIPrintPaper?](../uiprintinteractioncontroller/printpaper.md)
  An object that represents the paper size and printing area for the print job.
### Accessing information about the print job
- [var numberOfPages: Int](./numberofpages.md)
  The number of pages to render.
- [var paperRect: CGRect](./paperrect.md)
  The size of the paper for printing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiprintpagerenderer/printablerect)*