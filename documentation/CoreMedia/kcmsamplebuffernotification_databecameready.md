# kCMSampleBufferNotification_DataBecameReady

**Framework**: Core Media  
**Kind**: var  
**Role**: Global Variable

Posted on a sample buffer by the [`CMSampleBufferSetDataReady(_:)`](./cmsamplebuffersetdataready%28_%29.md) function when the buffer becomes ready.

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
let kCMSampleBufferNotification_DataBecameReady: CFString
```

```c
extern CFStringRef const kCMSampleBufferNotification_DataBecameReady;
```

## See Also

### Sample Buffer Notifications
- [let kCMSampleBufferNotification_DataFailed: CFString](./kcmsamplebuffernotification_datafailed.md)
- [let kCMSampleBufferNotificationParameter_OSStatus: CFString](./kcmsamplebuffernotificationparameter_osstatus.md)
- [let kCMSampleBufferConsumerNotification_BufferConsumed: CFString](./kcmsamplebufferconsumernotification_bufferconsumed.md)
  Optionally posted when a sample buffer is consumed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/kcmsamplebuffernotification_databecameready)*