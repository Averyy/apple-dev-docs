# PushToTalkTransmissionIntent

**Framework**: App Intents  
**Kind**: protocol

An intent that begins or ends an audio transmission with the Push to Talk framework.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- visionOS ?+

## Declaration

```swift
protocol PushToTalkTransmissionIntent : SystemIntent
```

#### Overview

Create an app intent that confirms to this protocol to manually start or end an audio transmission that uses the Push to Talk framework. For additional information about transmitting audio with the Push to Talk framework, see [`Push to Talk`](https://developer.apple.com/documentation/PushToTalk).

## Relationships

### Inherits From
- [AppIntent](appintent.md)
- [PersistentlyIdentifiable](persistentlyidentifiable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SystemIntent](systemintent.md)

## See Also

- [protocol ProgressReportingIntent](progressreportingintent.md)
  An intent that reports progress to the system during its execution
- [protocol ShowInAppSearchResultsIntent](showinappsearchresultsintent.md)
  An app intent that takes a person to search results for a specified search term.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/pushtotalktransmissionintent)*