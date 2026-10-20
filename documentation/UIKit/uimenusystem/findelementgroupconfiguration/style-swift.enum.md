# UIMenuSystem.FindElementGroupConfiguration.Style

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum UIMenuSystemFindElementGroupConfigurationStyle : NSInteger;
```

## Topics

### Enumeration Cases
- [UIMenuSystem.FindElementGroupConfiguration.Style.automatic](./style-swift.enum/automatic.md)
  The default preference. Find elements are automatically included based on the platform and other system behaviors.
- [UIMenuSystem.FindElementGroupConfiguration.Style.editableText](./style-swift.enum/editabletext.md)
  Prefer a full set of elements for finding and replacing text, such as Find, Find and Replace, Find Navigation, and so on.
- [UIMenuSystem.FindElementGroupConfiguration.Style.nonEditableText](./style-swift.enum/noneditabletext.md)
  Prefer a set of elements for finding within a non-editable text area
- [UIMenuSystem.FindElementGroupConfiguration.Style.search](./style-swift.enum/search.md)
  Prefer a minimal set of find elements, only consisting of elements to search content in the app.
### Initializers
- [init?(rawValue: Int)](./style-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../../Swift/bitwisecopyable.md)
- [Equatable](../../../Swift/equatable.md)
- [Hashable](../../../Swift/hashable.md)
- [RawRepresentable](../../../Swift/rawrepresentable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Inspecting a configuration of find elements
- [UIMenuSystem.FindElementGroupConfiguration](../findelementgroupconfiguration.md)
  Represents a configuration for find elements, should they be present. You don’t create one of these directly. A configuration is provided as part of a `UIMainMenuSystemConfiguration`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimenusystem/findelementgroupconfiguration/style-swift.enum)*