# CMSampleBufferInvalidateCallback

**Framework**: Core Media  
**Kind**: typealias

Client callback called by [`CMSampleBufferInvalidate(_:)`](cmsamplebufferinvalidate(_:).md).

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
typealias CMSampleBufferInvalidateCallback = (CMSampleBuffer, UInt64) -> Void
```

## Parameters

- `sbuf`: The   being invalidated.
- `invalidateRefCon`: Reference constant provided when the callback was set up.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsamplebufferinvalidatecallback)*