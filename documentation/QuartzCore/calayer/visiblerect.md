# visibleRect

**Framework**: Core Animation  
**Kind**: property

The visible region of the layer in its own coordinate space.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
var visibleRect: CGRect { get }
```

#### Discussion

The visible region is the area not clipped by the containing scroll layer.

## See Also

- [func scroll(CGPoint)](calayer/scroll(_:).md)
  Initiates a scroll in the layer’s closest ancestor scroll layer so that the specified point lies at the origin of the scroll layer.
- [func scrollRectToVisible(CGRect)](calayer/scrollrecttovisible(_:).md)
  Initiates a scroll in the layer’s closest ancestor scroll layer so that the specified rectangle becomes visible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/calayer/visiblerect)*