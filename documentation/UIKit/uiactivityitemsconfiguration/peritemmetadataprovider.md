# perItemMetadataProvider

**Framework**: UIKit  
**Kind**: property

A closure that provides metadata for each activity item.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var perItemMetadataProvider: ((Int, UIActivityItemsConfigurationMetadataKey) -> Any?)? { get set }
```

## Mentions

- [Collaborating and sharing copies of your data](collaborating-and-sharing-copies-of-your-data.md)

## See Also

- [var localObject: Any?](uiactivityitemsconfiguration/localobject.md)
  A local object that represents the configuration.
- [var metadataProvider: ((UIActivityItemsConfigurationMetadataKey) -> Any?)?](uiactivityitemsconfiguration/metadataprovider.md)
  A closure that provides metadata for the activity items.
- [var applicationActivitiesProvider: (() -> [UIActivity])?](uiactivityitemsconfiguration/applicationactivitiesprovider.md)
  A closure that provides application acitivites for the activity items.
- [struct UIActivityItemsConfigurationMetadataKey](uiactivityitemsconfigurationmetadatakey.md)
  A structure that defines keys for the metadata associated with an activity items configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiactivityitemsconfiguration/peritemmetadataprovider)*