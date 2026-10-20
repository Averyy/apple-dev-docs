# itemProvidersForActivityItemsConfiguration

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The item providers for the configuration.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var itemProvidersForActivityItemsConfiguration: [NSItemProvider] { get }
```

```objc
@property (nonatomic, copy, readonly) NSArray<NSItemProvider *> * itemProvidersForActivityItemsConfiguration;
```

## See Also

### Managing the Configuration
- [var applicationActivitiesForActivityItemsConfiguration: [UIActivity]?](./applicationactivitiesforactivityitemsconfiguration.md)
  The application activities, if any, for the configuration.
- [func activityItemsConfigurationMetadata(key: UIActivityItemsConfigurationMetadataKey) -> Any?](./activityitemsconfigurationmetadata%28key%29.md)
  Returns the configuration for the specified metadata key.
- [func activityItemsConfigurationMetadataForItem(at: Int, key: UIActivityItemsConfigurationMetadataKey) -> Any?](./activityitemsconfigurationmetadataforitem%28at,key%29.md)
  Returns the configuration for a particular item for the specified metadata key.
- [struct UIActivityItemsConfigurationMetadataKey](../uiactivityitemsconfigurationmetadatakey.md)
  A structure that defines keys for the metadata associated with an activity items configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiactivityitemsconfigurationreading/itemprovidersforactivityitemsconfiguration)*