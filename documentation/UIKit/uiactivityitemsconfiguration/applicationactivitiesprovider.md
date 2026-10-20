# applicationActivitiesProvider

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A closure that provides application acitivites for the activity items.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var applicationActivitiesProvider: (() -> [UIActivity])? { get set }
```

```objc
@property (nonatomic, strong, nullable) NSArray<UIActivity *> * (^applicationActivitiesProvider)();
```

## See Also

### Managing the configuration
- [var localObject: Any?](./localobject.md)
  A local object that represents the configuration.
- [var metadataProvider: ((UIActivityItemsConfigurationMetadataKey) -> Any?)?](./metadataprovider.md)
  A closure that provides metadata for the activity items.
- [var perItemMetadataProvider: ((Int, UIActivityItemsConfigurationMetadataKey) -> Any?)?](./peritemmetadataprovider.md)
  A closure that provides metadata for each activity item.
- [struct UIActivityItemsConfigurationMetadataKey](../uiactivityitemsconfigurationmetadatakey.md)
  A structure that defines keys for the metadata associated with an activity items configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiactivityitemsconfiguration/applicationactivitiesprovider)*