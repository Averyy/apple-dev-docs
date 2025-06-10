# flush(agedOutOnly:)

**Framework**: Core Video  
**Kind**: method

Frees as many buffers from the pool as possible.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
final func flush(agedOutOnly: Bool = true)
```

## Parameters

- `agedOutOnly`: Only free backings that are waiting to be aged out. If false, all unused backings are   flushed regardless of age.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvmutablepixelbuffer/pool/flush(agedoutonly:))*