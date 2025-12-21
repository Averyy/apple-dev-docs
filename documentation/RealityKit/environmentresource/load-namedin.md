# load(named:in:)

**Framework**: RealityKit  
**Kind**: method

Synchronously loads an environment resource from a bundle.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency static func load(named name: String, in bundle: Bundle? = nil) throws -> EnvironmentResource
```

#### Return Value

The environment resource that loads from the specified bundle.

#### Discussion

Loading an [`EnvironmentResource`](environmentresource.md) with this method blocks the main actor because it’s synchronous, so only call it from a command-line application. The method can stall a regular app, which makes it visibly hitch, and the system terminates an app if its UI becomes unresponsive.

If your image file is at the path `Foo.skybox/Bar.exr` in your Xcode project, use `Bar` for the name parameter.

To add an environment resource to your Xcode project, see [`EnvironmentResource`](environmentresource.md).

> ❗ **Important**: This function blocks the calling thread while RealityKit loads the requested resource.

## Parameters

- `name`: The image name without the file extension.
- `bundle`: The bundle to search for the resource. Use   to indicate the app’s bundle.

## See Also

- [convenience init(named: String, in: Bundle?) async throws](environmentresource/init(named:in:).md)
  Asynchronously loads an environment resource from a bundle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/environmentresource/load(named:in:))*