# delegate

**Framework**: Image Playground  
**Kind**: property

The delegate object that receives the generated image and handles events from the view controller.

**Availability**:
- iOS 18.1+
- iPadOS 18.1+
- Mac Catalyst 18.1+
- macOS 15.1+
- visionOS 2.4+

## Declaration

```swift
@MainActor
@objc @preconcurrency weak var delegate: (any ImagePlaygroundViewController.Delegate)?
```

#### Discussion

Set the value of this property to a custom type you define. The view controller reports relevant interactions to your type using the methods of the [`ImagePlaygroundViewController.Delegate`](imageplaygroundviewcontroller/delegate-swift.protocol.md) protocol. For example, the view controller notifies your delegate when the person accepts a generated image.

## See Also

- [ImagePlaygroundViewController.Delegate](imageplaygroundviewcontroller/delegate-swift.protocol.md)
  An interface you use to receive images and handle events related to an image-generation view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageplayground/imageplaygroundviewcontroller/delegate-swift.property)*