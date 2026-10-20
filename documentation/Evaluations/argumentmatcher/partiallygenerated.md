# ArgumentMatcher.PartiallyGenerated

**Framework**: Evaluations  
**Kind**: enum  
**Role**: Enumeration

A partially generated form of an argument matcher.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+
- Xcode 27.0+

## Declaration

```swift
nonisolated
enum PartiallyGenerated
```

## Topics

### Enumeration Cases
- [case contains(argumentName: String.PartiallyGenerated?, substring: String.PartiallyGenerated?)](./partiallygenerated/contains%28argumentname,substring%29.md)
  A partially generated contains argument matcher.
- [case exact(argumentName: String.PartiallyGenerated?, value: ArgumentValue.PartiallyGenerated?)](./partiallygenerated/exact%28argumentname,value%29.md)
  A partially generated exact-match argument matcher.
- [case hasPrefix(argumentName: String.PartiallyGenerated?, prefix: String.PartiallyGenerated?)](./partiallygenerated/hasprefix%28argumentname,prefix%29.md)
  A partially generated has-prefix argument matcher.
- [case hasSuffix(argumentName: String.PartiallyGenerated?, suffix: String.PartiallyGenerated?)](./partiallygenerated/hassuffix%28argumentname,suffix%29.md)
  A partially generated has-suffix argument matcher.
- [ArgumentMatcher.PartiallyGenerated.keyOnly(argumentName:)](./partiallygenerated/keyonly%28argumentname%29.md)
  A partially generated key-only argument matcher.
- [case naturalLanguage(argumentName: String.PartiallyGenerated?, criteria: String.PartiallyGenerated?)](./partiallygenerated/naturallanguage%28argumentname,criteria%29.md)
  A partially generated natural language argument matcher.
- [case oneOf(argumentName: String.PartiallyGenerated?, allowedValues: Array<ArgumentValue>.PartiallyGenerated?)](./partiallygenerated/oneof%28argumentname,allowedvalues%29.md)
  A partially generated one-of argument matcher.
- [case pattern(argumentName: String.PartiallyGenerated?, regex: String.PartiallyGenerated?)](./partiallygenerated/pattern%28argumentname,regex%29.md)
  A partially generated pattern argument matcher.
- [case range(argumentName: String.PartiallyGenerated?, minimum: Optional<Double>.PartiallyGenerated?, maximum: Optional<Double>.PartiallyGenerated?)](./partiallygenerated/range%28argumentname,minimum,maximum%29.md)
  A partially generated range argument matcher.
### Initializers
- [init(GeneratedContent) throws](./partiallygenerated/init%28_%29.md)
  Creates a partial argument matcher from the given generated content.

## Relationships

### Conforms To
- [ConvertibleFromGeneratedContent](../../FoundationModels/convertiblefromgeneratedcontent.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/argumentmatcher/partiallygenerated)*