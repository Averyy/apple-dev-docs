# printPageRenderer

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

Returns the page renderer for the print formatter.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
weak var printPageRenderer: UIPrintPageRenderer? { get }
```

```objc
@property (nonatomic, weak, readonly, nullable) UIPrintPageRenderer * printPageRenderer;
```

## Discussion

If the receiving print formatter was not added to a page renderer—that is, it was assigned to the [`printFormatter`](../uiprintinteractioncontroller/printformatter.md) property of the [`UIPrintInteractionController`](../uiprintinteractioncontroller.md) class—the value returned is `nil`.

## See Also

### Communicating with the page renderer
- [func removeFromPrintPageRenderer()](./removefromprintpagerenderer%28%29.md)
  Removes the print formatter from the page renderer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiprintformatter/printpagerenderer)*