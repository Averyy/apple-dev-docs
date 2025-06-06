# equalTo(_:equalityMask:)

**Framework**: Core Media  
**Kind**: method

Evaluates equality for the parts of two audio format descriptions.

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
func equalTo(_ otherFormatDescription: CMAudioFormatDescription, equalityMask: CMFormatDescription.EqualityMask = .all) -> (Bool, equalityMask: CMFormatDescription.EqualityMask)
```

## Parameters

- `otherFormatDescription`: A format description to compare.
- `equalityMask`: A mask that specifies which parts of the descriptions to compare.

## See Also

- [static func == (CMFormatDescription, CMFormatDescription) -> Bool](cmformatdescription/==(_:_:).md)
  Equality is derived from
- [func equalTo(CMFormatDescription, extensionKeysToIgnore: [CMFormatDescription.Extensions.Key], sampleDescriptionExtensionAtomKeysToIgnore: [String]) -> Bool](cmformatdescription/equalto(_:extensionkeystoignore:sampledescriptionextensionatomkeystoignore:).md)
  Evaluates equality for the parts of two audio format descriptions, ignoring the extensions you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmformatdescription/equalto(_:equalitymask:))*