# ==(_:_:)

**Framework**: Core Media  
**Kind**: op  
**Role**: Operator

Equality is derived from

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
static func == (lhs: CMFormatDescription, rhs: CMFormatDescription) -> Bool
```

## Discussion

```
lhs.equalTo(rhs,
            extensionKeysToIgnore: [],
            sampleDescriptionExtensionAtomKeysToIgnore: [])
```

## See Also

### Comparing Format Descriptions
- [func equalTo(CMAudioFormatDescription, equalityMask: CMFormatDescription.EqualityMask) -> (Bool, equalityMask: CMFormatDescription.EqualityMask)](./equalto%28_,equalitymask%29.md)
  Evaluates equality for the parts of two audio format descriptions.
- [func equalTo(CMFormatDescription, extensionKeysToIgnore: [CMFormatDescription.Extensions.Key], sampleDescriptionExtensionAtomKeysToIgnore: [String]) -> Bool](./equalto%28_,extensionkeystoignore,sampledescriptionextensionatomkeystoignore%29.md)
  Evaluates equality for the parts of two audio format descriptions, ignoring the extensions you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmformatdescription/==(_:_:))*