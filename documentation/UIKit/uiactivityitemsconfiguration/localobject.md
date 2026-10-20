# localObject

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A local object that represents the configuration.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var localObject: Any? { get set }
```

```objc
@property (nonatomic, strong, nullable) id localObject;
```

## See Also

### Managing the configuration
- [var metadataProvider: ((UIActivityItemsConfigurationMetadataKey) -> Any?)?](./metadataprovider.md)
  A closure that provides metadata for the activity items.
- [var perItemMetadataProvider: ((Int, UIActivityItemsConfigurationMetadataKey) -> Any?)?](./peritemmetadataprovider.md)
  A closure that provides metadata for each activity item.
- [var applicationActivitiesProvider: (() -> [UIActivity])?](./applicationactivitiesprovider.md)
  A closure that provides application acitivites for the activity items.
- [struct UIActivityItemsConfigurationMetadataKey](../uiactivityitemsconfigurationmetadatakey.md)
  A structure that defines keys for the metadata associated with an activity items configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiactivityitemsconfiguration/localobject)*