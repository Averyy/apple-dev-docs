# containerView

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The [`UIView`](../uiview.md) in which this layer is contained. This view is used to derive traits and other properties for applying the correct hover effect to the layer. It may also be used to assist with applying some kinds of hover effects to the layer.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
weak var containerView: UIView? { get set }
```

```objc
@property (nonatomic, weak, nullable) UIView * containerView;
```

#### Discussion

The [`containerView`](./containerview.md) should be an ancestor of this layer (once it has been added to a layer hierarchy) to behave correctly, but does not need to be the immediate parent of this layer. If the [`containerView`](./containerview.md) is set to nil or is deallocated, some aspects of this layer’s hover effect may no longer work correctly.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uihovereffectlayer/containerview)*