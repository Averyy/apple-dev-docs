# UIActivityItemsConfigurationMetadataKey

**Framework**: UIKit  
**Kind**: struct

A structure that defines keys for the metadata associated with an activity items configuration.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
struct UIActivityItemsConfigurationMetadataKey
```

## Topics

### Constants
- [static let title: UIActivityItemsConfigurationMetadataKey](uiactivityitemsconfigurationmetadatakey/title.md)
  A key for the title.
- [static let messageBody: UIActivityItemsConfigurationMetadataKey](uiactivityitemsconfigurationmetadatakey/messagebody.md)
  A key for the message body.
- [static let linkPresentationMetadata: UIActivityItemsConfigurationMetadataKey](uiactivityitemsconfigurationmetadatakey/linkpresentationmetadata.md)
- [static let shareRecipients: UIActivityItemsConfigurationMetadataKey](uiactivityitemsconfigurationmetadatakey/sharerecipients.md)
- [static let collaborationModeRestrictions: UIActivityItemsConfigurationMetadataKey](uiactivityitemsconfigurationmetadatakey/collaborationmoderestrictions.md)
  A key for a collaboration mode restriction, used to specify the case where Share Sheet should not support some modes of sharing even if they are supported by the items being shared The object returned for this key should be an array of UIActivityCollaborationModeRestriction instances For supported behaviour, this array should have a maximum size of one less than the amount of possible Share Sheet modes Currently at most one object should be provided
### Initializers
- [init(String)](uiactivityitemsconfigurationmetadatakey/init(_:).md)
  Creates an activity items configuration metadata key.
- [init(rawValue: String)](uiactivityitemsconfigurationmetadatakey/init(rawvalue:).md)
  Creates an activity items configuration metadata key with the specified raw value.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var localObject: Any?](uiactivityitemsconfiguration/localobject.md)
  A local object that represents the configuration.
- [var metadataProvider: ((UIActivityItemsConfigurationMetadataKey) -> Any?)?](uiactivityitemsconfiguration/metadataprovider.md)
  A closure that provides metadata for the activity items.
- [var perItemMetadataProvider: ((Int, UIActivityItemsConfigurationMetadataKey) -> Any?)?](uiactivityitemsconfiguration/peritemmetadataprovider.md)
  A closure that provides metadata for each activity item.
- [var applicationActivitiesProvider: (() -> [UIActivity])?](uiactivityitemsconfiguration/applicationactivitiesprovider.md)
  A closure that provides application acitivites for the activity items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiactivityitemsconfigurationmetadatakey)*