# UIPasteboard.OptionsKey

**Framework**: UIKit  
**Kind**: struct

Options for describing pasteboard privacy.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
struct OptionsKey
```

#### Overview

Use these options with the [`setItems(_:options:)`](uipasteboard/setitems(_:options:).md) method. Options that you set apply to all the items on a pasteboard.

## Topics

### Constants
- [static let expirationDate: UIPasteboard.OptionsKey](uipasteboard/optionskey/expirationdate.md)
  The time and date that you want the system to remove the pasteboard items from the pasteboard.
- [static let localOnly: UIPasteboard.OptionsKey](uipasteboard/optionskey/localonly.md)
  A Boolean value that specifies that the pasteboard items should not be available to other devices through the Handoff feature.
### Initializers
- [init(rawValue: String)](uipasteboard/optionskey/init(rawvalue:).md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [UIPasteboard.Name](uipasteboard/name-swift.struct.md)
  Constants that identify the name of a pasteboard.
- [Pasteboard Names](pasteboard-names.md)
  Names identifying the system pasteboards.
- [Pasteboard Data Type Representations](pasteboard-data-type-representations.md)
  Pasteboard-item representation types, as for a given object value.
- [UserInfo Dictionary Keys](userinfo-dictionary-keys.md)
  Use these keys to access the representation types of pasteboard items that you add to, or remove from, a pasteboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipasteboard/optionskey)*