# CMSampleBufferGetFormatDescription(_:)

**Framework**: Core Media  
**Kind**: func

Returns the format description of the samples in a sample buffer.

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
func CMSampleBufferGetFormatDescription(_ sbuf: CMSampleBuffer) -> CMFormatDescription?
```

#### Return Value

The format description of the samples in the `CMSampleBuffer` or `NULL` if there is an error.

#### Discussion

On return, the caller doesn’t own the returned `formatDesc`, and must retain it explicitly if the caller needs to maintain a reference to it.

## Parameters

- `sbuf`: The   being interrogated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsamplebuffergetformatdescription(_:))*