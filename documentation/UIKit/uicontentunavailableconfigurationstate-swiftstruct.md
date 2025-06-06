# UIContentUnavailableConfigurationState

**Framework**: UIKit  
**Kind**: struct

A structure that encapsulates state for a content-unavailable view.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- tvOS 17.0+
- visionOS ?+

## Declaration

```swift
struct UIContentUnavailableConfigurationState
```

#### Overview

Typically, you don’t create a configuration state yourself. To obtain a configuration state, override [`updateContentUnavailableConfiguration(using:)`](uiviewcontroller/updatecontentunavailableconfiguration(using:).md) in your view controller subclass and use the state parameter. Outside of this method, you can get a view controller’s configuration state from the [`contentUnavailableConfigurationState`](uiviewcontroller/contentunavailableconfigurationstate-7sczw.md) property.

You can create your own custom states to add to a content-unavailable configuration state by defining a custom state key with [`UIConfigurationStateCustomKey`](uiconfigurationstatecustomkey.md).

## Topics

### Instance Properties
- [var searchText: String?](uicontentunavailableconfigurationstate-swift.struct/searchtext.md)
  The search text.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomReflectable](../Swift/CustomReflectable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [UIConfigurationState](uiconfigurationstate-8d7pd.md)

## See Also

- [struct UIContentUnavailableConfiguration](uicontentunavailableconfiguration-swift.struct.md)
  A content configuration for a content-unavailable view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicontentunavailableconfigurationstate-swift.struct)*