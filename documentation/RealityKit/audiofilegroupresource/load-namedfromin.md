# load(named:from:in:)

**Framework**: RealityKit  
**Kind**: method

Loads an audio resource from a Reality Composer Pro project.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency static func load(named name: String, from scene: String, in bundle: Bundle? = nil) throws -> AudioFileGroupResource
```

#### Discussion

This method loads a preconfigured [`AudioFileGroupResource`](audiofilegroupresource.md) from a scene in a Reality Composer Pro project.

> ❗ **Important**: The name provided  be unique.

## Parameters

- `name`: The USD Prim path to the resource in the Reality Composer Pro project to load.
- `scene`: The name of the Reality Composer Pro scene to load from.
- `bundle`: The bundle that contains the project. Leave   to load from the app’s bundle.

## See Also

- [init([AudioFileResource]) throws](audiofilegroupresource/init(_:).md)
  Creates a group resource from an array of audio file resources.
- [convenience init(named: String, from: String, in: Bundle) async throws](audiofilegroupresource/init(named:from:in:).md)
  Initializes an audio resource from a Reality Composer Pro project.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/audiofilegroupresource/load(named:from:in:))*