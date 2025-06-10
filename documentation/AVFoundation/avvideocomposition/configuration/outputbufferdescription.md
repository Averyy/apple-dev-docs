# outputBufferDescription

**Framework**: AVFoundation  
**Kind**: property

The output buffers of the video composition can be specified with the outputBufferDescription. The value is an array of an array of CMTag objects that describes the output buffers.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
var outputBufferDescription: [[CMTag]]? { get set }
```

#### Return Value

A description of the output buffers.

#### Discussion

If the video composition will output tagged buffers, the details of those buffers should be specified with CMTags. Specifically, the StereoView (eyes) must be specified. The behavior is undefined if the output buffers do not match the outputBufferDescription. The default is nil, which means monoscopic output. Note that an empty array is not valid. Note that tagged buffers are only supported for custom compositors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avvideocomposition/configuration/outputbufferdescription)*