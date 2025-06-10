# loadAsync(named:in:)

**Framework**: RealityKit  
**Kind**: method

Asynchronously loads an environment resource from a bundle.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+ (Beta)
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency static func loadAsync(named name: String, in bundle: Bundle? = nil) -> LoadRequest<EnvironmentResource>
```

#### Return Value

The environment resource that loads from the specified bundle.

#### Discussion

If your image file is at the path `Foo.skybox/Bar.exr` in your Xcode project, use `Bar` for the name parameter. You need to call this function with the `async` keyword from an asynchronous context, such as from within a [`Task`](https://developer.apple.com/documentation/Swift/Task) closure.

To add an environment resource to your Xcode project, see [`EnvironmentResource`](environmentresource.md).

## Parameters

- `name`: The image name without the file extension.
- `bundle`: The bundle to search for the resource. Use   to indicate the app’s bundle.

## See Also

- [static func generate(fromEquirectangular: CGImage, withName: String?) throws -> EnvironmentResource](environmentresource/generate(fromequirectangular:withname:)-3wtpe.md)
  Synchronously generates an environment resource from an equirectangular image.
- [static func generate(fromEquirectangular: CGImage, withName: String?) async throws -> EnvironmentResource](environmentresource/generate(fromequirectangular:withname:)-6mxsi.md)
  Asynchronously generates an environment resource from an equirectangular image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/environmentresource/loadasync(named:in:))*