# IntentDonationIdentifier

**Framework**: App Intents  
**Kind**: struct  
**Role**: Structure

An opaque type that identifies a specific donation to the system.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS
- watchOS 9.0+

## Declaration

```swift
struct IntentDonationIdentifier
```

#### Overview

When you donate an app intent, the system returns a unique `IntentDonationIdentifier` instance so you can refer to that donation later. Use that instance to identify the donation later, and to delete it using an [`IntentDonationManager`](./intentdonationmanager.md) if the action no longer applies.

## Relationships

### Conforms To
- [Decodable](../Swift/decodable.md)
- [Encodable](../Swift/encodable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Donation management
- [struct IntentDonationManager](./intentdonationmanager.md)
  A type you use to teach the system about the actions people take using your app.
- [struct IntentDonationMatchingPredicate](./intentdonationmatchingpredicate.md)
  A type you use to specify previously donated app intents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentdonationidentifier)*