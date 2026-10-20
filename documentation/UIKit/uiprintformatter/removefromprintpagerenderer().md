# removeFromPrintPageRenderer()

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Removes the print formatter from the page renderer.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func removeFromPrintPageRenderer()
```

```objc
- (void) removeFromPrintPageRenderer;
```

#### Discussion

A print formatter is typically associated with a pages of a [`UIPrintPageRenderer`](../uiprintpagerenderer.md) object through the [`addPrintFormatter(_:startingAtPageAt:)`](../uiprintpagerenderer/addprintformatter%28_,startingatpageat%29.md) method.

## See Also

### Communicating with the page renderer
- [var printPageRenderer: UIPrintPageRenderer?](./printpagerenderer.md)
  Returns the page renderer for the print formatter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiprintformatter/removefromprintpagerenderer())*