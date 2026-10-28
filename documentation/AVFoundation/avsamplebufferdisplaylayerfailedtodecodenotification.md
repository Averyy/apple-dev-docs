# AVSampleBufferDisplayLayerFailedToDecodeNotification

**Framework**: AVFoundation  
**Kind**: var  
**Role**: Global Variable

A notification the system posts when a sample buffer display layer fails to decode.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 10.2+
- visionOS 1.0+

## Declaration

```c
extern NSString * const AVSampleBufferDisplayLayerFailedToDecodeNotification;
```

## Discussion

You can retrieve the error object from the user information dictionary by querying it for its [`AVSampleBufferDisplayLayerFailedToDecodeNotificationErrorKey`](./avsamplebufferdisplaylayerfailedtodecodenotificationerrorkey.md) value.

## See Also

### Handling errors
- [let AVSampleBufferDisplayLayerFailedToDecodeNotificationErrorKey: String](./avsamplebufferdisplaylayerfailedtodecodenotificationerrorkey.md)
  The key for the corresponding error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebufferdisplaylayerfailedtodecodenotification)*