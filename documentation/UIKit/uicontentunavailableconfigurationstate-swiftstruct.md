# UIContentUnavailableConfigurationState

**Framework**: UIKit  
**Kind**: struct

A structure that encapsulates state for a content-unavailable view.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
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
- [Copyable](../swift/copyable.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomReflectable](../swift/customreflectable.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Escapable](../swift/escapable.md)
- [Hashable](../swift/hashable.md)
- [UIConfigurationState](uiconfigurationstate-8d7pd.md)

## See Also

- [struct UIContentUnavailableConfiguration](uicontentunavailableconfiguration-swift.struct.md)
  A content configuration for a content-unavailable view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicontentunavailableconfigurationstate-swift.struct)*