# init(equirectangular:options:)

**Framework**: RealityKit  
**Kind**: init

Asynchronously generates an environment resource from an equirectangular image.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
@MainActor
convenience init(equirectangular cgImage: CGImage, options: EnvironmentResource.CreateOptions) async throws
```

## Parameters

- `cgImage`: The source equirectangular (latitude, longitude) image. To preserve all details use an image where the width is half the height.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/environmentresource/init(equirectangular:options:))*