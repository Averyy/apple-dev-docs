# init(input:configuration:)

**Framework**: RealityKit  
**Kind**: init  
**Role**: Initializer

Creates a session from a specified directory of images.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
convenience init(input: URL, configuration: PhotogrammetrySession.Configuration = Configuration()) throws
```

**Other overloads**:

```swift
convenience init<S>(input: S, configuration: PhotogrammetrySession.Configuration = Configuration()) throws where S : Sequence, S.Element == PhotogrammetrySample
```

## Discussion

Creates a new session instance using all images in the specified [`URL`](../../Foundation/url.md) input directory [`URL`](../../Foundation/url.md) as samples for reconstruction.

> **Throws**: If `input` is not a file [`URL`](../../Foundation/url.md).

## Parameters

- `input`: The directory [`URL`](../../Foundation/url.md) containing a folder of images to use as reconstruction inputs.
- `configuration`: The configuration to use for this session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/photogrammetrysession/init(input:configuration:))*