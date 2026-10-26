# MERAWProcessorReadyForMoreMediaDataDidChangeNotification

**Framework**: MediaExtension  
**Kind**: var  
**Role**: Global Variable

A notification that indicates a change to the object’s readiness to process additional media data.

**Availability**:
- macOS 15.0+

## Declaration

```c
extern NSNotificationName const MERAWProcessorReadyForMoreMediaDataDidChangeNotification;
```

#### Discussion

This notification is used to notify Video Toolbox that the value of the [`isReadyForMoreMediaData`](./merawprocessor/isreadyformoremediadata.md) property has changed.

## See Also

### Notifications
- [MERAWProcessorValuesDidChangeNotification](./merawprocessorvaluesdidchangenotification.md)
  A notification that indicates a change to the object’s set of available processing parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/merawprocessorreadyformoremediadatadidchangenotification)*