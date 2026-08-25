# ArgumentMatcher.PartiallyGenerated

**Framework**: Evaluations  
**Kind**: enum

A partially generated form of an argument matcher.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)
- Xcode 27.0+ (Beta)

## Declaration

```swift
nonisolated
enum PartiallyGenerated
```

## Topics

### Enumeration Cases
- [case contains(argumentName: String.PartiallyGenerated?, substring: String.PartiallyGenerated?)](argumentmatcher/partiallygenerated/contains(argumentname:substring:).md)
  A partially generated contains argument matcher.
- [case exact(argumentName: String.PartiallyGenerated?, value: ArgumentValue.PartiallyGenerated?)](argumentmatcher/partiallygenerated/exact(argumentname:value:).md)
  A partially generated exact-match argument matcher.
- [case hasPrefix(argumentName: String.PartiallyGenerated?, prefix: String.PartiallyGenerated?)](argumentmatcher/partiallygenerated/hasprefix(argumentname:prefix:).md)
  A partially generated has-prefix argument matcher.
- [case hasSuffix(argumentName: String.PartiallyGenerated?, suffix: String.PartiallyGenerated?)](argumentmatcher/partiallygenerated/hassuffix(argumentname:suffix:).md)
  A partially generated has-suffix argument matcher.
- [ArgumentMatcher.PartiallyGenerated.keyOnly(argumentName:)](argumentmatcher/partiallygenerated/keyonly(argumentname:).md)
  A partially generated key-only argument matcher.
- [case naturalLanguage(argumentName: String.PartiallyGenerated?, criteria: String.PartiallyGenerated?)](argumentmatcher/partiallygenerated/naturallanguage(argumentname:criteria:).md)
  A partially generated natural language argument matcher.
- [case oneOf(argumentName: String.PartiallyGenerated?, allowedValues: Array<ArgumentValue>.PartiallyGenerated?)](argumentmatcher/partiallygenerated/oneof(argumentname:allowedvalues:).md)
  A partially generated one-of argument matcher.
- [case pattern(argumentName: String.PartiallyGenerated?, regex: String.PartiallyGenerated?)](argumentmatcher/partiallygenerated/pattern(argumentname:regex:).md)
  A partially generated pattern argument matcher.
- [case range(argumentName: String.PartiallyGenerated?, minimum: Optional<Double>.PartiallyGenerated?, maximum: Optional<Double>.PartiallyGenerated?)](argumentmatcher/partiallygenerated/range(argumentname:minimum:maximum:).md)
  A partially generated range argument matcher.
### Initializers
- [init(GeneratedContent) throws](argumentmatcher/partiallygenerated/init(_:).md)
  Creates a partial argument matcher from the given generated content.

## Relationships

### Conforms To
- [ConvertibleFromGeneratedContent](../foundationmodels/convertiblefromgeneratedcontent.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/argumentmatcher/partiallygenerated)*