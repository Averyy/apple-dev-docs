# ToolExpectation.PartiallyGenerated

**Framework**: Evaluations  
**Kind**: enum  
**Role**: Enumeration

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
- [case anyOrder(expectations: Array<ToolExpectation>.PartiallyGenerated?)](./partiallygenerated/anyorder%28expectations%29.md)
  A partially generated group of tool expectations that can match in any order.
- [case expectation(name: String.PartiallyGenerated?, arguments: Array<ArgumentMatcher>.PartiallyGenerated?)](./partiallygenerated/expectation%28name,arguments%29.md)
  A partially generated single tool expectation with an optional name and arguments.
### Initializers
- [init(GeneratedContent) throws](./partiallygenerated/init%28_%29.md)
  Creates a partial tool expectation from the given generated content.

## Relationships

### Conforms To
- [ConvertibleFromGeneratedContent](../../FoundationModels/convertiblefromgeneratedcontent.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/toolexpectation/partiallygenerated)*