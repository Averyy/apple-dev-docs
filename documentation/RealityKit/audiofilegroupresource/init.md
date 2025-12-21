# init(_:)

**Framework**: RealityKit  
**Kind**: init

Creates a group resource from an array of audio file resources.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency init(_ resources: [AudioFileResource]) throws
```

#### Discussion

An [`AudioFileGroupResource`](audiofilegroupresource.md) provides a single, random element from its collection of [`AudioFileResource`](audiofileresource.md) objects each time [`play()`](audioplaybackcontroller/play().md) is called on the [`AudioPlaybackController`](audioplaybackcontroller.md) on which it is prepared.

> **Note**: An error if the provided array is empty or if the underlying audio assets do not have matching channel layouts.

## See Also

- [convenience init(named: String, from: String, in: Bundle) async throws](audiofilegroupresource/init(named:from:in:).md)
  Initializes an audio resource from a Reality Composer Pro project.
- [static func load(named: String, from: String, in: Bundle?) throws -> AudioFileGroupResource](audiofilegroupresource/load(named:from:in:).md)
  Loads an audio resource from a Reality Composer Pro project.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/audiofilegroupresource/init(_:))*