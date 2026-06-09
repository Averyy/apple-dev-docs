# init(_:)

**Framework**: RealityKit  
**Kind**: init

Creates a group resource from an array of audio file resources (backward compatibility).

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

This initializer maintains backward compatibility with existing code that doesn’t specify configuration.

> **Note**: An error if the provided array is empty or if the underlying audio assets do not have matching channel layouts.

## Parameters

- `resources`: The audio file resources for the group

## See Also

- [convenience init(named: String, from: String, in: Bundle) async throws](audiofilegroupresource/init(named:from:in:).md)
  Initializes an audio resource from a Reality Composer Pro project.
- [static func load(named: String, from: String, in: Bundle?) throws -> AudioFileGroupResource](audiofilegroupresource/load(named:from:in:).md)
  Loads an audio resource from a Reality Composer Pro project.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/audiofilegroupresource/init(_:))*