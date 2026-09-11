# ToolExpectation.PartiallyGenerated

**Framework**: Evaluations  
**Kind**: enum

A partially generated form of a tool expectation.

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