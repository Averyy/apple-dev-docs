# UINib.OptionsKey

**Framework**: UIKit  
**Kind**: struct

Options that specify how to unarchive and instantiate the nib.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
struct OptionsKey
```

## Topics

### Keys
- [static let externalObjects: UINib.OptionsKey](uinib/optionskey/externalobjects.md)
  The replacements for any proxy objects in the nib file.
### Initializers
- [init(rawValue: String)](uinib/optionskey/init(rawvalue:).md)
  Creates a new instance with the specified raw value.

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [func instantiate(withOwner: Any?, options: [UINib.OptionsKey : Any]?) -> [Any]](uinib/instantiate(withowner:options:).md)
  Unarchives and instantiates the in-memory contents of the nib object’s nib file, creating a distinct object tree and set of top-level objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinib/optionskey)*