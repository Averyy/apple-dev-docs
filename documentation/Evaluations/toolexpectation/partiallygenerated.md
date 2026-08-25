# ToolExpectation.PartiallyGenerated

**Framework**: Evaluations  
**Kind**: enum

A partially generated form of a tool expectation.

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
- [case anyOrder(expectations: Array<ToolExpectation>.PartiallyGenerated?)](toolexpectation/partiallygenerated/anyorder(expectations:).md)
  A partially generated group of tool expectations that can match in any order.
- [case expectation(name: String.PartiallyGenerated?, arguments: Array<ArgumentMatcher>.PartiallyGenerated?)](toolexpectation/partiallygenerated/expectation(name:arguments:).md)
  A partially generated single tool expectation with an optional name and arguments.
### Initializers
- [init(GeneratedContent) throws](toolexpectation/partiallygenerated/init(_:).md)
  Creates a partial tool expectation from the given generated content.

## Relationships

### Conforms To
- [ConvertibleFromGeneratedContent](../foundationmodels/convertiblefromgeneratedcontent.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/toolexpectation/partiallygenerated)*