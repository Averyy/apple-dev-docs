# CMSampleBufferInvalidateCallback

**Framework**: Core Media  
**Kind**: typealias  
**Role**: Type Alias

Client callback called by [`CMSampleBufferInvalidate(_:)`](./cmsamplebufferinvalidate%28_%29.md).

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

```c
typedef void (*)(struct opaqueCMSampleBuffer *, unsigned long long) CMSampleBufferInvalidateCallback;
```

## Parameters

- `sbuf`: The `CMSampleBuffer` being invalidated.
- `invalidateRefCon`: Reference constant provided when the callback was set up.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsamplebufferinvalidatecallback)*