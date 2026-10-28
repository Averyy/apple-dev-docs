# MEVideoDecoderReadyForMoreMediaDataDidChangeNotification

**Framework**: MediaExtension  
**Kind**: var  
**Role**: Global Variable

A notification that indicates a change to the decoder’s readiness to process additional media data.

**Availability**:
- macOS 14.0+

## Declaration

```c
extern NSNotificationName const MEVideoDecoderReadyForMoreMediaDataDidChangeNotification;
```

## Discussion

This notification is used to notify the Video Toolbox that the value of the [`isReadyForMoreMediaData`](./mevideodecoder/isreadyformoremediadata.md) property has changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/mevideodecoderreadyformoremediadatadidchangenotification)*