# UIActivityItemsConfiguration

**Framework**: UIKit  
**Kind**: class

A configuration that allows a responder to export data through a variety of interactions.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UIActivityItemsConfiguration
```

## Mentions

- [Collaborating and sharing copies of your data](collaborating-and-sharing-copies-of-your-data.md)

## Topics

### Creating an activity items configuration
- [init(objects: [any NSItemProviderWriting])](uiactivityitemsconfiguration/init(objects:).md)
  Initializes and returns an activity items configuration with the specified objects.
- [init(itemProviders: [NSItemProvider])](uiactivityitemsconfiguration/init(itemproviders:).md)
  Initializes and returns an activity items configuration with the specified item providers.
### Managing the configuration
- [var localObject: Any?](uiactivityitemsconfiguration/localobject.md)
  A local object that represents the configuration.
- [var metadataProvider: ((UIActivityItemsConfigurationMetadataKey) -> Any?)?](uiactivityitemsconfiguration/metadataprovider.md)
  A closure that provides metadata for the activity items.
- [var perItemMetadataProvider: ((Int, UIActivityItemsConfigurationMetadataKey) -> Any?)?](uiactivityitemsconfiguration/peritemmetadataprovider.md)
  A closure that provides metadata for each activity item.
- [var applicationActivitiesProvider: (() -> [UIActivity])?](uiactivityitemsconfiguration/applicationactivitiesprovider.md)
  A closure that provides application acitivites for the activity items.
- [struct UIActivityItemsConfigurationMetadataKey](uiactivityitemsconfigurationmetadatakey.md)
  A structure that defines keys for the metadata associated with an activity items configuration.
### Managing supported interactions
- [var supportedInteractions: [UIActivityItemsConfigurationInteraction]](uiactivityitemsconfiguration/supportedinteractions.md)
  The types of interactions that the configuration supports.
- [struct UIActivityItemsConfigurationInteraction](uiactivityitemsconfigurationinteraction.md)
  A structure that describes types of interactions.
### Managing previews
- [var previewProvider: ((Int, UIActivityItemsConfigurationPreviewIntent, CGSize) -> NSItemProvider?)?](uiactivityitemsconfiguration/previewprovider.md)
  A closure that provides previews for the activity items.
- [struct UIActivityItemsConfigurationPreviewIntent](uiactivityitemsconfigurationpreviewintent.md)
  A structure that specifies the types of activity item previews.
### Restricting the sharing mode
- [UIActivityViewController.CollaborationModeRestriction](uiactivityviewcontroller/collaborationmoderestriction.md)
  An object that disables the sharing mode and optionally displays an alert.
- [enum UIActivityCollaborationMode](uiactivitycollaborationmode.md)
  A value that defines how the system shares an item.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [UIActivityItemsConfigurationReading](uiactivityitemsconfigurationreading.md)

## See Also

- [init(activityItems: [Any], applicationActivities: [UIActivity]?)](uiactivityviewcontroller/init(activityitems:applicationactivities:).md)
  Initializes a new activity view controller object that acts on the specified data.
- [convenience init(activityItemsConfiguration: any UIActivityItemsConfigurationReading)](uiactivityviewcontroller/init(activityitemsconfiguration:).md)
  Initializes a new activity view controller object that acts on the specified configuration.
- [protocol UIActivityItemsConfigurationReading](uiactivityitemsconfigurationreading.md)
  A set of methods adopted by an object so that the object can act as an activity items configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiactivityitemsconfiguration)*