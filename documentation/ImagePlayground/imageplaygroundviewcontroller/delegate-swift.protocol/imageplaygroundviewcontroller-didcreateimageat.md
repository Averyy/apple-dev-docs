# imagePlaygroundViewController(_:didCreateImageAt:)

**Framework**: Image Playground  
**Kind**: method  
**Required**: Yes

Returns the generated image to the delegate.

**Availability**:
- iOS 18.1+
- iPadOS 18.1+
- Mac Catalyst 18.1+
- macOS 15.1+
- visionOS 2.4+

## Declaration

```swift
@MainActor
@objc func imagePlaygroundViewController(_ imagePlaygroundViewController: ImagePlaygroundViewController, didCreateImageAt imageURL: URL)
```

#### Discussion

Use this method to retrieve the image at the specified location. After you finish retrieving the image, dismiss the [`ImagePlaygroundViewController`](imageplaygroundviewcontroller.md) from your app’s interface.

## Parameters

- `imagePlaygroundViewController`: The view controller that sent the   notification.
- `imageURL`: The location of the generated image. The file will live inside   a temporary folder of your app sandbox. The app should move it to a   permanent location or clean it up when it has finished using the file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageplayground/imageplaygroundviewcontroller/delegate-swift.protocol/imageplaygroundviewcontroller(_:didcreateimageat:))*