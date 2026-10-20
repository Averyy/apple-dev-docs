# AVVideoEncoderSpecificationKey

**Framework**: AVFoundation  
**Kind**: var  
**Role**: Global Variable

The video encoder specification includes options for choosing a specific video encoder.

**Availability**:
- macOS 10.10+

## Declaration

```swift
let AVVideoEncoderSpecificationKey: String
```

```c
extern NSString * const AVVideoEncoderSpecificationKey;
```

#### Discussion

The value for this key is a dictionary containing `kVTVideoEncoderSpecification_*` keys specified in the VideoToolbox framework. This key should be specified at the top level of an `AVVideoSettings` dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avvideoencoderspecificationkey)*