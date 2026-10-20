# activityItemsConfigurationMetadata(key:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Returns the configuration for the specified metadata key.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
optional func activityItemsConfigurationMetadata(key: UIActivityItemsConfigurationMetadataKey) -> Any?
```

```objc
- (id) activityItemsConfigurationMetadataForKey:(UIActivityItemsConfigurationMetadataKey) key;
```

## See Also

### Managing the Configuration
- [var itemProvidersForActivityItemsConfiguration: [NSItemProvider]](./itemprovidersforactivityitemsconfiguration.md)
  The item providers for the configuration.
- [var applicationActivitiesForActivityItemsConfiguration: [UIActivity]?](./applicationactivitiesforactivityitemsconfiguration.md)
  The application activities, if any, for the configuration.
- [func activityItemsConfigurationMetadataForItem(at: Int, key: UIActivityItemsConfigurationMetadataKey) -> Any?](./activityitemsconfigurationmetadataforitem%28at,key%29.md)
  Returns the configuration for a particular item for the specified metadata key.
- [struct UIActivityItemsConfigurationMetadataKey](../uiactivityitemsconfigurationmetadatakey.md)
  A structure that defines keys for the metadata associated with an activity items configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiactivityitemsconfigurationreading/activityitemsconfigurationmetadata(key:))*