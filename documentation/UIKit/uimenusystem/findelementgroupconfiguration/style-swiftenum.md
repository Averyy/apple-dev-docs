# UIMenuSystem.FindElementGroupConfiguration.Style

**Framework**: UIKit  
**Kind**: enum

Represents a preference for the structure of Find elements in the main menu.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
enum Style
```

## Topics

### Enumeration Cases
- [UIMenuSystem.FindElementGroupConfiguration.Style.automatic](uimenusystem/findelementgroupconfiguration/style-swift.enum/automatic.md)
  The default preference. Find elements are automatically included based on the platform and other system behaviors.
- [UIMenuSystem.FindElementGroupConfiguration.Style.editableText](uimenusystem/findelementgroupconfiguration/style-swift.enum/editabletext.md)
  Prefer a full set of elements for finding and replacing text, such as Find, Find and Replace, Find Navigation, and so on.
- [UIMenuSystem.FindElementGroupConfiguration.Style.nonEditableText](uimenusystem/findelementgroupconfiguration/style-swift.enum/noneditabletext.md)
  Prefer a set of elements for finding within a non-editable text area
- [UIMenuSystem.FindElementGroupConfiguration.Style.search](uimenusystem/findelementgroupconfiguration/style-swift.enum/search.md)
  Prefer a minimal set of find elements, only consisting of elements to search content in the app.
### Initializers
- [init?(rawValue: Int)](uimenusystem/findelementgroupconfiguration/style-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [UIMenuSystem.FindElementGroupConfiguration](uimenusystem/findelementgroupconfiguration.md)
  Represents a configuration for find elements, should they be present. You don’t create one of these directly. A configuration is provided as part of a `UIMainMenuSystemConfiguration`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimenusystem/findelementgroupconfiguration/style-swift.enum)*