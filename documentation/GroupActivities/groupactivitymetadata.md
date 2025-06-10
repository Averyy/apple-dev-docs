# GroupActivityMetadata

**Framework**: Group Activities  
**Kind**: struct

Text and image content that describes an activity to potential participants.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
struct GroupActivityMetadata
```

## Mentions

- [Defining your app’s SharePlay activities](defining-your-apps-shareplay-activities.md)
- [Adding spatial Persona support to an activity](adding-spatial-persona-support-to-an-activity.md)

#### Overview

Use a `GroupActivityMetadata` structure to store user-facing information about a specific activity your app suggests. Metadata information includes the title of the activity, an image that corresponds to the activity, and a fallback URL for users who don’t have your app. For example, a movie-watching activity might include the poster of the specific movie a participant suggests. The system uses the provided metadata to generate invitations for other participants.

Create a `GroupActivityMetadata` structure in the [`metadata`](groupactivity/metadata.md) property of your custom [`GroupActivity`](groupactivity.md) subclass. Populate the new structure with the relevant data for your activity.

## Topics

### Creating group activity metadata
- [init()](groupactivitymetadata/init.md)
  Creates a new instance for storing descriptive information about an activity.
- [init(from: any Decoder) throws](groupactivitymetadata/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Presenting the activity
- [var title: String?](groupactivitymetadata/title.md)
  The localized string to display as the title of your activity.
- [var subtitle: String?](groupactivitymetadata/subtitle.md)
  The localized string that provides additional information about the activity.
- [var previewImage: CGImage?](groupactivitymetadata/previewimage.md)
  The image to display for the current activity.
- [var fallbackURL: URL?](groupactivitymetadata/fallbackurl.md)
  A URL that offers participants a way to identify or join the activity from a web browser.
### Indicating the activity’s type
- [var type: GroupActivityMetadata.ActivityType](groupactivitymetadata/type.md)
  The type of shared experience.
- [GroupActivityMetadata.ActivityType](groupactivitymetadata/activitytype.md)
  Constants that indicate the group activity’s type to the system.
### Assigning an app-specific scene
- [var sceneAssociationBehavior: SceneAssociationBehavior](groupactivitymetadata/sceneassociationbehavior.md)
  Criteria the system uses to direct an activity to a specific scene of your app.
- [struct SceneAssociationBehavior](sceneassociationbehavior.md)
  A type that tells the system which scene to associate with an incoming group activity.
### Specifying media-related behavior
- [var supportsContinuationOnTV: Bool](groupactivitymetadata/supportscontinuationontv.md)
  A Boolean value that indicates whether your app supports activity continuation on an Apple TV.
- [var preferredBroadcastOptions: BroadcastOptions](groupactivitymetadata/preferredbroadcastoptions.md)
  Preferences for how to present audio and video on the main communication channel.
- [struct BroadcastOptions](broadcastoptions.md)
  Options for how to broadcast media on the shared communications channel.
### Comparing metadata objects
- [static func != (Self, Self) -> Bool](groupactivitymetadata/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.
- [static func == (GroupActivityMetadata, GroupActivityMetadata) -> Bool](groupactivitymetadata/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Encoding the metadata
- [func encode(to: any Encoder) throws](groupactivitymetadata/encode(to:).md)
  Encodes this value into the given encoder.
### Structures
- [GroupActivityMetadata.LifetimePolicy](groupactivitymetadata/lifetimepolicy-swift.struct.md)
  An activity lifetime policy used by a Group Activity.
### Instance Properties
- [var experience: GroupActivityMetadata.Experience?](groupactivitymetadata/experience-swift.property.md)
- [var lifetimePolicy: GroupActivityMetadata.LifetimePolicy](groupactivitymetadata/lifetimepolicy-swift.property.md)
  Determines how an activity can be ended.
- [var localizedSubtitle: String?](groupactivitymetadata/localizedsubtitle.md)
- [var localizedTitle: String?](groupactivitymetadata/localizedtitle.md)
### Enumerations
- [GroupActivityMetadata.Experience](groupactivitymetadata/experience-swift.enum.md)
### Default Implementations
- [Decodable Implementations](groupactivitymetadata/decodable-implementations.md)
- [Encodable Implementations](groupactivitymetadata/encodable-implementations.md)
- [Equatable Implementations](groupactivitymetadata/equatable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Defining your app’s SharePlay activities](defining-your-apps-shareplay-activities.md)
  Configure your app’s SharePlay support and define the activities that people can perform from your app.
- [Supporting Coordinated Media Playback](../AVFoundation/supporting-coordinated-media-playback.md)
  Create synchronized media experiences that enable users to watch and listen across devices.
- [protocol GroupActivity](groupactivity.md)
  A type that can advertise your app’s activities to other participants.
- [enum GroupActivityActivationResult](groupactivityactivationresult.md)
  The result of preparing to start a custom activity.
- [struct GroupActivityTransferRepresentation](groupactivitytransferrepresentation.md)
  A type that lets you start a group activity from a known context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/groupactivitymetadata)*