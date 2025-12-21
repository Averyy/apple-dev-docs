# flush(agedOutOnly:)

**Framework**: Core Video  
**Kind**: method

Frees as many buffers from the pool as possible.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
final func flush(agedOutOnly: Bool = true)
```

## Parameters

- `agedOutOnly`: Only free backings that are waiting to be aged out. If false, all unused backings are   flushed regardless of age.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvmutablepixelbuffer/pool/flush(agedoutonly:))*