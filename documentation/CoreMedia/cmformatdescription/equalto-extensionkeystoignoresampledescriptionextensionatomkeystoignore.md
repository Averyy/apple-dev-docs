# equalTo(_:extensionKeysToIgnore:sampleDescriptionExtensionAtomKeysToIgnore:)

**Framework**: Core Media  
**Kind**: method

Evaluates equality for the parts of two audio format descriptions, ignoring the extensions you specify.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst ?+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func equalTo(_ otherFormatDescription: CMFormatDescription, extensionKeysToIgnore: [CMFormatDescription.Extensions.Key] = [], sampleDescriptionExtensionAtomKeysToIgnore: [String] = []) -> Bool
```

## Parameters

- `otherFormatDescription`: A format description to compare to.
- `extensionKeysToIgnore`: A list of format description extension keys.
- `sampleDescriptionExtensionAtomKeysToIgnore`: A list of sample description extension atom keys.

## See Also

- [static func == (CMFormatDescription, CMFormatDescription) -> Bool](cmformatdescription/==(_:_:).md)
  Equality is derived from
- [func equalTo(CMAudioFormatDescription, equalityMask: CMFormatDescription.EqualityMask) -> (Bool, equalityMask: CMFormatDescription.EqualityMask)](cmformatdescription/equalto(_:equalitymask:).md)
  Evaluates equality for the parts of two audio format descriptions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmformatdescription/equalto(_:extensionkeystoignore:sampledescriptionextensionatomkeystoignore:))*