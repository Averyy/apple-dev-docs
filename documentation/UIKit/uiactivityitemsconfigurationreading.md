# UIActivityItemsConfigurationReading

**Framework**: UIKit  
**Kind**: protocol

A set of methods adopted by an object so that the object can act as an activity items configuration.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
protocol UIActivityItemsConfigurationReading : NSObjectProtocol
```

## Topics

### Managing the Configuration
- [var itemProvidersForActivityItemsConfiguration: [NSItemProvider]](uiactivityitemsconfigurationreading/itemprovidersforactivityitemsconfiguration.md)
  The item providers for the configuration.
- [var applicationActivitiesForActivityItemsConfiguration: [UIActivity]?](uiactivityitemsconfigurationreading/applicationactivitiesforactivityitemsconfiguration.md)
  The application activities, if any, for the configuration.
- [func activityItemsConfigurationMetadata(key: UIActivityItemsConfigurationMetadataKey) -> Any?](uiactivityitemsconfigurationreading/activityitemsconfigurationmetadata(key:).md)
  Returns the configuration for the specified metadata key.
- [func activityItemsConfigurationMetadataForItem(at: Int, key: UIActivityItemsConfigurationMetadataKey) -> Any?](uiactivityitemsconfigurationreading/activityitemsconfigurationmetadataforitem(at:key:).md)
  Returns the configuration for a particular item for the specified metadata key.
- [struct UIActivityItemsConfigurationMetadataKey](uiactivityitemsconfigurationmetadatakey.md)
  A structure that defines keys for the metadata associated with an activity items configuration.
### Managing Supported Interactions
- [func activityItemsConfigurationSupports(interaction: UIActivityItemsConfigurationInteraction) -> Bool](uiactivityitemsconfigurationreading/activityitemsconfigurationsupports(interaction:).md)
  Returns a Boolean value that indicates whether the activity items configuration supports the specified type of interaction.
- [struct UIActivityItemsConfigurationInteraction](uiactivityitemsconfigurationinteraction.md)
  A structure that describes types of interactions.
### Managing Previews
- [func activityItemsConfigurationPreviewForItem(at: Int, intent: UIActivityItemsConfigurationPreviewIntent, suggestedSize: CGSize) -> NSItemProvider?](uiactivityitemsconfigurationreading/activityitemsconfigurationpreviewforitem(at:intent:suggestedsize:).md)
  Returns an activity items configuration preview for the specified item and preview size.
- [struct UIActivityItemsConfigurationPreviewIntent](uiactivityitemsconfigurationpreviewintent.md)
  A structure that specifies the types of activity item previews.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Conforming Types
- [UIActivityItemsConfiguration](uiactivityitemsconfiguration.md)

## See Also

- [init(activityItems: [Any], applicationActivities: [UIActivity]?)](uiactivityviewcontroller/init(activityitems:applicationactivities:).md)
  Initializes a new activity view controller object that acts on the specified data.
- [convenience init(activityItemsConfiguration: any UIActivityItemsConfigurationReading)](uiactivityviewcontroller/init(activityitemsconfiguration:).md)
  Initializes a new activity view controller object that acts on the specified configuration.
- [class UIActivityItemsConfiguration](uiactivityitemsconfiguration.md)
  A configuration that allows a responder to export data through a variety of interactions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiactivityitemsconfigurationreading)*