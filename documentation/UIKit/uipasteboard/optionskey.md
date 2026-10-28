# UIPasteboard.OptionsKey

**Framework**: UIKit  
**Kind**: struct  
**Role**: Structure

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

```c
typedef NSString * UIPasteboardOption;
```

## Overview

Use these options with the [`setItems(_:options:)`](./setitems%28_,options%29.md) method. Options that you set apply to all the items on a pasteboard.

## Topics

### Constants
- [static let expirationDate: UIPasteboard.OptionsKey](./optionskey/expirationdate.md)
  The time and date that you want the system to remove the pasteboard items from the pasteboard.
- [static let localOnly: UIPasteboard.OptionsKey](./optionskey/localonly.md)
  A Boolean value that specifies that the pasteboard items should not be available to other devices through the Handoff feature.
### Initializers
- [init(rawValue: String)](./optionskey/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Constants
- [UIPasteboard.Name](./name-swift.struct.md)
  Constants that identify the name of a pasteboard.
- [Pasteboard Names](../pasteboard-names.md)
  Names identifying the system pasteboards.
- [Pasteboard Data Type Representations](../pasteboard-data-type-representations.md)
  Pasteboard-item representation types, as for a given object value.
- [UserInfo Dictionary Keys](../userinfo-dictionary-keys.md)
  Use these keys to access the representation types of pasteboard items that you add to, or remove from, a pasteboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipasteboard/optionskey)*