# init(outputSettings:)

**Framework**: AVFoundation  
**Kind**: init

Creates a video output object initialized with the specified output settings.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
init(outputSettings: [String : any Sendable]?)
```

#### Discussion

For uncompressed video output, start with `kCVPixelBuffer*` keys in `<CoreVideo/CVPixelBuffer.h>`. In addition to the keys in `CVPixelBuffer.h`, uncompressed video settings dictionaries may also provide a value for [`AVVideoAllowWideColorKey`](avvideoallowwidecolorkey.md).

## Parameters

- `outputSettings`: The client requirements for output   objects, expressed using the constants in  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritemvideooutput/init(outputsettings:))*