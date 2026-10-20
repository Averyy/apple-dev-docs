# isDecodable

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the track is decodable in the current environment.

**Availability**:
- iOS 11.0+ - Deprecated in 16.0
- iPadOS 11.0+ - Deprecated in 16.0
- Mac Catalyst 13.1+ - Deprecated in 16.0
- macOS 10.13+ - Deprecated in 13.0
- tvOS 11.0+ - Deprecated in 16.0
- watchOS 4.0+ - Deprecated in 9.0

> **Deprecated**: Load the value of [`isDecodable`](../avpartialasyncproperty/isdecodable.md) asynchronously instead.

## Declaration

```swift
var isDecodable: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isDecodable) BOOL decodable;
```

#### Discussion

When this property is [`true`](../../Swift/true.md), the system can decode the track, even if decoding may be too slow for real-time playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassettrack/isdecodable)*