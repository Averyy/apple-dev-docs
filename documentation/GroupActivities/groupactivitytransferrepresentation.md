# GroupActivityTransferRepresentation

**Framework**: Group Activities  
**Kind**: struct  
**Role**: Structure

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

## Topics

### Initializers
- [init<ActivityType>(exporting: (Item) async throws -> ActivityType)](./groupactivitytransferrepresentation/init%28exporting%29.md)
  Creates a type that exports a group activity for the specified item.

## Relationships

### Conforms To
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [TransferRepresentation](../CoreTransferable/transferrepresentation.md)

## See Also

### Activity definition
- [Defining your app’s SharePlay activities](./defining-your-apps-shareplay-activities.md)
  Configure your app’s SharePlay support and define the activities that people can perform from your app.
- [Supporting coordinated media playback](../AVFoundation/supporting-coordinated-media-playback.md)
  Create synchronized media experiences that enable users to watch and listen across devices.
- [protocol GroupActivity](./groupactivity.md)
  A type that can advertise your app’s activities to other participants.
- [struct GroupActivityMetadata](./groupactivitymetadata.md)
  Text and image content that describes an activity to potential participants.
- [enum GroupActivityActivationResult](./groupactivityactivationresult.md)
  The result of preparing to start a custom activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/groupactivitytransferrepresentation)*