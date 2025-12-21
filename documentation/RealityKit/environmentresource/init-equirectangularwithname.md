# init(equirectangular:withName:)

**Framework**: RealityKit  
**Kind**: init

Asynchronously generates an environment resource from an equirectangular image.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
@MainActor
@preconcurrency convenience init(equirectangular cgImage: CGImage, withName resourceName: String? = nil) async throws
```

## Parameters

- `cgImage`: The source equirectangular (latitude, longitude) image. To preserve all details use an image where the width is half the height.
- `resourceName`: A unique name the method assigns to the resource it loads,   for use in network synchronization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/environmentresource/init(equirectangular:withname:))*