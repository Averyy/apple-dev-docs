# FeatureSet.ContentVersion

**Framework**: PaperKit  
**Kind**: enum

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
enum ContentVersion
```

## Topics

### Enumeration Cases
- [FeatureSet.ContentVersion.version1](featureset/contentversion-swift.enum/version1.md)
  The PaperKit version that supports markup.
### Initializers
- [init?(rawValue: Int)](featureset/contentversion-swift.enum/init(rawvalue:).md)
  Creates a new instance with the specified raw value.
### Instance Properties
- [var pencilKitContentVersion: PKContentVersion](featureset/contentversion-swift.enum/pencilkitcontentversion.md)
  The PencilKit content version that this PaperKit version relies on.
- [var rawValue: Int](featureset/contentversion-swift.enum/rawvalue-swift.property.md)
  The corresponding value of the raw type.
### Type Aliases
- [FeatureSet.ContentVersion.RawValue](featureset/contentversion-swift.enum/rawvalue-swift.typealias.md)
  The raw type that can be used to represent all values of the conforming type.
### Type Properties
- [static var latest: FeatureSet.ContentVersion](featureset/contentversion-swift.enum/latest.md)
  A property that returns latest version of PaperKit, which supports all currently available features.
### Default Implementations
- [Equatable Implementations](featureset/contentversion-swift.enum/equatable-implementations.md)
- [RawRepresentable Implementations](featureset/contentversion-swift.enum/rawrepresentable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/featureset/contentversion-swift.enum)*