# GroupActivityTransferRepresentation

**Framework**: Group Activities  
**Kind**: struct

A type that lets you start a group activity from a known context.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
struct GroupActivityTransferRepresentation<Item> where Item : Transferable
```

## Mentions

- [Defining your app’s SharePlay activities](defining-your-apps-shareplay-activities.md)
- [Presenting SharePlay activities from your app’s UI](promoting-shareplay-activities-from-your-apps-ui.md)

## Topics

### Initializers
- [init<ActivityType>(exporting: (Item) async throws -> ActivityType)](groupactivitytransferrepresentation/init(exporting:).md)
  Creates a type that exports a group activity for the specified item.
### Instance Properties
- [var body: some TransferRepresentation](groupactivitytransferrepresentation/body-swift.property.md)
  A builder expression that describes the process of importing and exporting an item.
### Type Aliases
- [GroupActivityTransferRepresentation.Body](groupactivitytransferrepresentation/body-swift.typealias.md)
  The transfer representation for the item.
### Default Implementations
- [TransferRepresentation Implementations](groupactivitytransferrepresentation/transferrepresentation-implementations.md)

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [TransferRepresentation](../CoreTransferable/TransferRepresentation.md)

## See Also

- [Defining your app’s SharePlay activities](defining-your-apps-shareplay-activities.md)
  Configure your app’s SharePlay support and define the activities that people can perform from your app.
- [Supporting Coordinated Media Playback](../AVFoundation/supporting-coordinated-media-playback.md)
  Create synchronized media experiences that enable users to watch and listen across devices.
- [protocol GroupActivity](groupactivity.md)
  A type that can advertise your app’s activities to other participants.
- [struct GroupActivityMetadata](groupactivitymetadata.md)
  Text and image content that describes an activity to potential participants.
- [enum GroupActivityActivationResult](groupactivityactivationresult.md)
  The result of preparing to start a custom activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/groupactivitytransferrepresentation)*