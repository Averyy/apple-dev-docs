# applicationActivitiesForActivityItemsConfiguration

**Framework**: UIKit  
**Kind**: property

The application activities, if any, for the configuration.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional var applicationActivitiesForActivityItemsConfiguration: [UIActivity]? { get }
```

## See Also

- [var itemProvidersForActivityItemsConfiguration: [NSItemProvider]](uiactivityitemsconfigurationreading/itemprovidersforactivityitemsconfiguration.md)
  The item providers for the configuration.
- [func activityItemsConfigurationMetadata(key: UIActivityItemsConfigurationMetadataKey) -> Any?](uiactivityitemsconfigurationreading/activityitemsconfigurationmetadata(key:).md)
  Returns the configuration for the specified metadata key.
- [func activityItemsConfigurationMetadataForItem(at: Int, key: UIActivityItemsConfigurationMetadataKey) -> Any?](uiactivityitemsconfigurationreading/activityitemsconfigurationmetadataforitem(at:key:).md)
  Returns the configuration for a particular item for the specified metadata key.
- [struct UIActivityItemsConfigurationMetadataKey](uiactivityitemsconfigurationmetadatakey.md)
  A structure that defines keys for the metadata associated with an activity items configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiactivityitemsconfigurationreading/applicationactivitiesforactivityitemsconfiguration)*