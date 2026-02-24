# ==(_:_:)

**Framework**: Core Media  
**Kind**: op

Equality is derived from

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
static func == (lhs: CMFormatDescription, rhs: CMFormatDescription) -> Bool
```

#### Discussion

```None
lhs.equalTo(rhs,
            extensionKeysToIgnore: [],
            sampleDescriptionExtensionAtomKeysToIgnore: [])
```

## See Also

- [func equalTo(CMAudioFormatDescription, equalityMask: CMFormatDescription.EqualityMask) -> (Bool, equalityMask: CMFormatDescription.EqualityMask)](cmformatdescription/equalto(_:equalitymask:).md)
  Evaluates equality for the parts of two audio format descriptions.
- [func equalTo(CMFormatDescription, extensionKeysToIgnore: [CMFormatDescription.Extensions.Key], sampleDescriptionExtensionAtomKeysToIgnore: [String]) -> Bool](cmformatdescription/equalto(_:extensionkeystoignore:sampledescriptionextensionatomkeystoignore:).md)
  Evaluates equality for the parts of two audio format descriptions, ignoring the extensions you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmformatdescription/==(_:_:))*