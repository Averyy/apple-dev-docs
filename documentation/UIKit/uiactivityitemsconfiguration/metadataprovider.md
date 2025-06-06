# metadataProvider

**Framework**: UIKit  
**Kind**: property

A closure that provides metadata for the activity items.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var metadataProvider: ((UIActivityItemsConfigurationMetadataKey) -> Any?)? { get set }
```

## See Also

- [var localObject: Any?](uiactivityitemsconfiguration/localobject.md)
  A local object that represents the configuration.
- [var perItemMetadataProvider: ((Int, UIActivityItemsConfigurationMetadataKey) -> Any?)?](uiactivityitemsconfiguration/peritemmetadataprovider.md)
  A closure that provides metadata for each activity item.
- [var applicationActivitiesProvider: (() -> [UIActivity])?](uiactivityitemsconfiguration/applicationactivitiesprovider.md)
  A closure that provides application acitivites for the activity items.
- [struct UIActivityItemsConfigurationMetadataKey](uiactivityitemsconfigurationmetadatakey.md)
  A structure that defines keys for the metadata associated with an activity items configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiactivityitemsconfiguration/metadataprovider)*