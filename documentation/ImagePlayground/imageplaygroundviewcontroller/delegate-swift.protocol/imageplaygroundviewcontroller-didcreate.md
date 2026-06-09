# imagePlaygroundViewController(_:didCreate:)

**Framework**: Image Playground  
**Kind**: method

Returns the generated genmoji to the delegate.

**Availability**:
- iOS 18.1+
- iPadOS 18.1+
- Mac Catalyst 18.1+
- macOS 15.1+
- visionOS 2.4+

## Declaration

```swift
@MainActor
@objc optional func imagePlaygroundViewController(_ imagePlaygroundViewController: ImagePlaygroundViewController, didCreate adaptiveImageGlyph: NSAdaptiveImageGlyph)
```

#### Discussion

Use this method to access the genmoji. After you finish retrieving the image, dismiss the [`ImagePlaygroundViewController`](imageplaygroundviewcontroller.md) from your app’s interface.

## Parameters

- `imagePlaygroundViewController`: The view controller that sent the notification.
- `adaptiveImageGlyph`: The adaptive image glyph that represents the generated genmoji.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageplayground/imageplaygroundviewcontroller/delegate-swift.protocol/imageplaygroundviewcontroller(_:didcreate:))*