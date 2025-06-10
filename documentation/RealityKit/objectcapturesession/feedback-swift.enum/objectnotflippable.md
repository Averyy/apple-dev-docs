# ObjectCaptureSession.Feedback.objectNotFlippable

**Framework**: RealityKit  
**Kind**: case

It is not recommended to flip this object since is is unlikely the algorithm will be able to stitch the flipped orientation.  This is usually due to feature-less, low-texture objects.  In this case, multiple passes at different heights leaving object at its original orientation are recommended instead of flipping.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+

## Declaration

```swift
case objectNotFlippable
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/objectcapturesession/feedback-swift.enum/objectnotflippable)*