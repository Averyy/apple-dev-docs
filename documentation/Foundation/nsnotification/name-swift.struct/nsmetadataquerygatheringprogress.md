# NSMetadataQueryGatheringProgress

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

Posted as the receiver is collecting results during the initial result-gathering phase of the query.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static let NSMetadataQueryGatheringProgress: NSNotification.Name
```

```c
extern NSNotificationName const NSMetadataQueryGatheringProgressNotification;
```

## See Also

### Working with notifications
- [static let NSMetadataQueryDidFinishGathering: NSNotification.Name](./nsmetadataquerydidfinishgathering.md)
  Posted when the receiver has finished with the initial result-gathering phase of the query.
- [static let NSMetadataQueryDidStartGathering: NSNotification.Name](./nsmetadataquerydidstartgathering.md)
  Posted when the receiver begins with the initial result-gathering phase of the query.
- [static let NSMetadataQueryDidUpdate: NSNotification.Name](./nsmetadataquerydidupdate.md)
  Posted when the receiver’s results have changed during the live-update phase of the query.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsnotification/name-swift.struct/nsmetadataquerygatheringprogress)*