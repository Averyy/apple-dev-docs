# init()

**Framework**: Image Playground  
**Kind**: init

Creates a new image creator object for you to use in your app.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
init() async throws
```

#### Discussion

If the device doesn’t support image creation or the feature is currently unavailable, this initializer throws an error.

> **Note**: `ImageCreator.Error.notSupported` on iOS 27.0+, macOS 27.0+, and visionOS 27.0+.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageplayground/imagecreator/init())*