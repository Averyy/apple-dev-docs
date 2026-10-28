# paperRect

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The size of the paper for printing.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var paperRect: CGRect { get }
```

```objc
@property (nonatomic, readonly) CGRect paperRect;
```

## Discussion

The value of this property is a rectangle that defines the size of paper chosen for the print job. The origin is always (0,0).

## See Also

### Related Documentation
- [var printPaper: UIPrintPaper?](../uiprintinteractioncontroller/printpaper.md)
  An object that represents the paper size and printing area for the print job.
### Accessing information about the print job
- [var numberOfPages: Int](./numberofpages.md)
  The number of pages to render.
- [var printableRect: CGRect](./printablerect.md)
  The area in which printing can occur.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiprintpagerenderer/paperrect)*