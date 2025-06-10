# init(named:from:in:)

**Framework**: RealityKit  
**Kind**: init

Initializes an audio resource from a Reality Composer Pro project.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency convenience init(named name: String, from scene: String, in bundle: Bundle) async throws
```

#### Discussion

This method initializes a preconfigured [`AudioFileGroupResource`](audiofilegroupresource.md) from a scene in a Reality Composer Pro project.

> ❗ **Important**: The name provided  be unique.

## Parameters

- `name`: The USD Prim path to the resource in the Reality Composer Pro project to initialize.
- `scene`: The name of the Reality Composer Pro scene to initialize from.
- `bundle`: The bundle that contains the project.

## See Also

- [init([AudioFileResource]) throws](audiofilegroupresource/init(_:).md)
  Creates a group resource from an array of audio file resources.
- [static func load(named: String, from: String, in: Bundle?) throws -> AudioFileGroupResource](audiofilegroupresource/load(named:from:in:).md)
  Loads an audio resource from a Reality Composer Pro project.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/audiofilegroupresource/init(named:from:in:))*