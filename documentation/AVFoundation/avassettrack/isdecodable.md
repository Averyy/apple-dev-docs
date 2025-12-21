# isDecodable

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that indicates whether the track is decodable in the current environment.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- watchOS 4.0+

## Declaration

```swift
var isDecodable: Bool { get }
```

#### Discussion

When this property is [`true`](https://developer.apple.com/documentation/Swift/true), the system can decode the track, even if decoding may be too slow for real-time playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassettrack/isdecodable)*