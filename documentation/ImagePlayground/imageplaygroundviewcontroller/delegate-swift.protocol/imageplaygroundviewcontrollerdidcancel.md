# imagePlaygroundViewControllerDidCancel(_:)

**Framework**: Image Playground  
**Kind**: method

Notifies the delegate that the person canceled the generation of the image.

**Availability**:
- iOS 18.1+
- iPadOS 18.1+
- Mac Catalyst 18.1+
- macOS 15.1+
- visionOS 2.4+

## Declaration

```swift
@MainActor
@objc optional func imagePlaygroundViewControllerDidCancel(_ imagePlaygroundViewController: ImagePlaygroundViewController)
```

#### Discussion

Use this method to dismiss the specified [`ImagePlaygroundViewController`](imageplaygroundviewcontroller.md) from your app’s interface.

## Parameters

- `imagePlaygroundViewController`: The view controller that sent   the notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageplayground/imageplaygroundviewcontroller/delegate-swift.protocol/imageplaygroundviewcontrollerdidcancel(_:))*