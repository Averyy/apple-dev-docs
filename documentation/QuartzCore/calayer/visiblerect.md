# visibleRect

**Framework**: Core Animation  
**Kind**: property  
**Role**: Instance Property

The visible region of the layer in its own coordinate space.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
var visibleRect: CGRect { get }
```

```objc
@property (readonly) CGRect visibleRect;
```

## Discussion

The visible region is the area not clipped by the containing scroll layer.

## See Also

### Scrolling
- [func scroll(CGPoint)](./scroll%28_%29.md)
  Initiates a scroll in the layer’s closest ancestor scroll layer so that the specified point lies at the origin of the scroll layer.
- [func scrollRectToVisible(CGRect)](./scrollrecttovisible%28_%29.md)
  Initiates a scroll in the layer’s closest ancestor scroll layer so that the specified rectangle becomes visible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/calayer/visiblerect)*