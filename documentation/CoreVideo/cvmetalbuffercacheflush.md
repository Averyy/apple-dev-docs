# CVMetalBufferCacheFlush(_:_:)

**Framework**: Core Video  
**Kind**: func

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
func CVMetalBufferCacheFlush(_ bufferCache: CVMetalBufferCache, _ options: CVOptionFlags)
```

#### Discussion

Performs internal housekeeping/recycling operations

This call must be made periodically to give the buffer cache a chance to do internal housekeeping operations.

## Parameters

- `bufferCache`: The buffer cache object to flush
- `options`: Currently unused, set to 0.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvmetalbuffercacheflush(_:_:))*