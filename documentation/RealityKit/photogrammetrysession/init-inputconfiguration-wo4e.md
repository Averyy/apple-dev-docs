# init(input:configuration:)

**Framework**: RealityKit  
**Kind**: init

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

#### Discussion

Creates a new session instance using all images in the specified [`URL`](https://developer.apple.com/documentation/Foundation/URL) input directory [`URL`](https://developer.apple.com/documentation/Foundation/URL) as samples for reconstruction.

> **Note**: If `input` is not a file [`URL`](https://developer.apple.com/documentation/Foundation/URL).

If `input` is not a file [`URL`](https://developer.apple.com/documentation/Foundation/URL).

## Parameters

- `input`: The directory   containing a folder of images to use as reconstruction inputs.
- `configuration`: The configuration to use for this session.

## See Also

- [convenience init<S>(input: S, configuration: PhotogrammetrySession.Configuration) throws](photogrammetrysession/init(input:configuration:)-7glmh.md)
  Creates a session from a sequence of samples.
- [static var isSupported: Bool](photogrammetrysession/issupported.md)
  Returns `true` if the current hardware supports Object Capture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/photogrammetrysession/init(input:configuration:)-wo4e)*