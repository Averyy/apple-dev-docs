# UIPasteboard.Name

**Framework**: UIKit  
**Kind**: struct  
**Role**: Structure

Constants that identify the name of a pasteboard.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- visionOS

## Declaration

```swift
struct Name
```

```c
typedef NSString * UIPasteboardName;
```

## Topics

### Names
- [static let general: UIPasteboard.Name](./name-swift.struct/general.md)
  The name identifying the general pasteboard, which you use for general copy-cut-paste operations.
### Initializers
- [init(String)](./name-swift.struct/init%28_%29.md)
- [init(rawValue: String)](./name-swift.struct/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Constants
- [Pasteboard Names](../pasteboard-names.md)
  Names identifying the system pasteboards.
- [UIPasteboard.OptionsKey](./optionskey.md)
  Options for describing pasteboard privacy.
- [Pasteboard Data Type Representations](../pasteboard-data-type-representations.md)
  Pasteboard-item representation types, as for a given object value.
- [UserInfo Dictionary Keys](../userinfo-dictionary-keys.md)
  Use these keys to access the representation types of pasteboard items that you add to, or remove from, a pasteboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipasteboard/name-swift.struct)*