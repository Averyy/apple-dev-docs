# UINib.OptionsKey

**Framework**: UIKit  
**Kind**: struct  
**Role**: Structure

Options that specify how to unarchive and instantiate the nib.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
struct OptionsKey
```

```c
typedef NSString * UINibOptionsKey;
```

## Topics

### Keys
- [static let externalObjects: UINib.OptionsKey](./optionskey/externalobjects.md)
  The replacements for any proxy objects in the nib file.
### Initializers
- [init(rawValue: String)](./optionskey/init%28rawvalue%29.md)
  Creates a new instance with the specified raw value.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Retrieving objects from the nib file
- [func instantiate(withOwner: Any?, options: [UINib.OptionsKey : Any]?) -> [Any]](./instantiate%28withowner,options%29.md)
  Unarchives and instantiates the in-memory contents of the nib object’s nib file, creating a distinct object tree and set of top-level objects.
- [UINibProxiedObjectsKey](../uinibproxiedobjectskey.md)
  The runtime replacement objects for any proxy objects in the nib file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinib/optionskey)*