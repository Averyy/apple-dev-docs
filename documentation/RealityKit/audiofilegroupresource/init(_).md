# init(_:)

**Framework**: RealityKit  
**Kind**: init  
**Role**: Initializer

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

## Discussion

This initializer maintains backward compatibility with existing code that doesn’t specify configuration.

> **Throws**: An error if the provided array is empty or if the underlying audio assets do not have matching channel layouts.

## Parameters

- `resources`: The audio file resources for the group

## See Also

### Creating a resource
- [convenience init(named: String, from: String, in: Bundle) async throws](./init%28named,from,in%29.md)
  Initializes an audio resource from a Reality Composer Pro project.
- [static func load(named: String, from: String, in: Bundle?) throws -> AudioFileGroupResource](./load%28named,from,in%29.md)
  Loads an audio resource from a Reality Composer Pro project.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/audiofilegroupresource/init(_:))*