# ProgressReportingIntent

**Framework**: App Intents  
**Kind**: protocol

An intent that reports progress to the system during its execution

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- macOS 14.0+
- tvOS 17.0+
- visionOS ?+
- watchOS 10.0+

## Declaration

```swift
protocol ProgressReportingIntent : AppIntent
```

## Topics

### Instance Properties
- [var progress: Progress](progressreportingintent/progress.md)
  An object representing the progress of the intent’s action.

## Relationships

### Inherits From
- [AppIntent](appintent.md)
- [PersistentlyIdentifiable](persistentlyidentifiable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
### Inherited By
- [LongRunningIntent](longrunningintent.md)

## See Also

- [protocol PushToTalkTransmissionIntent](pushtotalktransmissionintent.md)
  An intent that begins or ends an audio transmission with the Push to Talk framework.
- [protocol ShowInAppSearchResultsIntent](showinappsearchresultsintent.md)
  An app intent that takes a person to search results for a specified search term.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/progressreportingintent)*