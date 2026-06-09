# init(rawValue:)

**Framework**: ScreenCaptureKit  
**Kind**: init

Creates a new instance with a raw value.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 18.2+
- macOS 12.3+
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
init(rawValue: String)
```

#### Discussion

> ❗ **Important**:  Use the static properties of [`SCStreamFrameInfo`](scstreamframeinfo.md) such as [`status`](scstreamframeinfo/status.md) or [`contentRect`](scstreamframeinfo/contentrect.md) instead of creating an instance with this initializer.

## Parameters

- `rawValue`: The raw value to use for the new instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scstreamframeinfo/init(rawvalue:))*