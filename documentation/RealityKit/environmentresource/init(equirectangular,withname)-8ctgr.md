# init(equirectangular:withName:)

**Framework**: RealityKit  
**Kind**: init  
**Role**: Initializer

Synchronously creates an environment resource from an equirectangular image.

**Availability**:
- iOS 18.0+ - Deprecated in 27.2
- iPadOS 18.0+ - Deprecated in 27.2
- Mac Catalyst 18.0+
- macOS 15.0+ - Deprecated in 27.2
- tvOS 26.0+ - Deprecated in 27.2
- visionOS 2.0+ - Deprecated in 27.2

> **Deprecated**: Use `init(equirectangular:options:)` instead. Will be deprecated to support skybox-free EnvironmentResource.

## Declaration

```swift
@MainActor
@preconcurrency convenience init(equirectangular cgImage: CGImage, withName resourceName: String? = nil) throws
```

**Other overloads**:

```swift
@MainActor
@preconcurrency convenience init(equirectangular cgImage: CGImage, withName resourceName: String? = nil) async throws
```

## Discussion

Loading an [`EnvironmentResource`](../environmentresource.md) with this method blocks the main actor because it’s synchronous, so only call it from a command-line application. The method can stall a regular app, which makes it visibly hitch, and the system terminates an app if its UI becomes unresponsive.

## Parameters

- `cgImage`: The source equirectangular (latitude, longitude) image. To preserve all details use an image where the width is half the height.
- `resourceName`: A unique name the method assigns to the resource it loads, for use in network synchronization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/environmentresource/init(equirectangular:withname:)-8ctgr)*