# timebase

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The renderer’s timebase, which determines how the layer interprets time stamps.

**Availability**:
- iOS 8.0+ - Deprecated in 18.0
- iPadOS 8.0+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.8+ - Deprecated in 15.0
- tvOS 10.2+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0

> **Deprecated**: Use sampleBufferRenderer's timebase instead

## Declaration

```swift
var timebase: CMTimebase { get }
```

```objc
@property (retain, readonly) CMTimebaseRef timebase;
```

#### Discussion

Apple discourages the use of this symbol in iOS 17, tvOS 17, and macOS 14 and later. Use [`timebase`](../avqueuedsamplebufferrendering/timebase.md) on the [`sampleBufferRenderer`](./samplebufferrenderer.md) instead.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebufferdisplaylayer/timebase)*