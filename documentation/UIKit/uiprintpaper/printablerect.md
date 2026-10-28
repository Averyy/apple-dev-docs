# printableRect

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The rectangle that represents the portion of the paper that can be imaged upon.

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
@property (readonly) CGRect printableRect;
```

## Discussion

Typically, UIKit passes this value into the last argument of the [`UIPrintPageRenderer`](../uiprintpagerenderer.md) method [`drawPage(at:in:)`](../uiprintpagerenderer/drawpage%28at,in%29.md).

## See Also

### Getting the paper size and the printing area
- [var paperSize: CGSize](./papersize.md)
  The size of the sheet to use for printing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiprintpaper/printablerect)*