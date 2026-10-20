# init()

**Framework**: Image Playground  
**Kind**: init  
**Role**: Initializer

Creates a new image creator object for you to use in your app.

**Availability**:
- iOS 18.4+ - Deprecated in 27.0
- iPadOS 18.4+ - Deprecated in 27.0
- Mac Catalyst 18.4+ - Deprecated in 27.0
- macOS 15.4+ - Deprecated in 27.0
- visionOS 2.4+ - Deprecated in 27.0

## Declaration

```swift
init() async throws
```

#### Discussion

If the device doesn’t support image creation or the feature is currently unavailable, this initializer throws an error.

> **Throws**: `ImageCreator.Error.notSupported` on iOS 27.0+, macOS 27.0+, and visionOS 27.0+.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageplayground/imagecreator/init())*