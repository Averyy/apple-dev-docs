# AttachmentContentBuilder

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

A result builder that creates attachment content from closures.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
@resultBuilder
struct AttachmentContentBuilder
```

#### Overview

The `buildBlock` methods in this type create [`AttachmentContent`](./attachmentcontent.md) instances based on the number and types of sources provided as parameters.

RealityKit calls this builder for you when SwiftUI annotates the `attachment` parameter of some [`RealityView`](./realityview.md) initializers that have the `@AttachmentContentBuilder` annotation.

## Topics

### Type Methods
- [static func buildBlock() -> EmptyAttachmentContent](./attachmentcontentbuilder/buildblock%28%29.md)
  Creates an empty attachment content containing no statements.
- [static buildBlock(_:)](./attachmentcontentbuilder/buildblock%28_%29.md)
  Creates a single content result.
- [static func buildEither<TrueContent, FalseContent>(first: TrueContent) -> ConditionalAttachmentContent<TrueContent, FalseContent>](./attachmentcontentbuilder/buildeither%28first%29.md)
  Provides support for “if” statements in multi-statement closures, producing conditional content for the “then” branch.
- [static func buildEither<TrueContent, FalseContent>(second: FalseContent) -> ConditionalAttachmentContent<TrueContent, FalseContent>](./attachmentcontentbuilder/buildeither%28second%29.md)
  Provides support for “if-else” statements in multi-statement closures, producing conditional content for the “else” branch.
- [static func buildExpression<Content>(Content) -> Content](./attachmentcontentbuilder/buildexpression%28_%29.md)
  Builds an expression within the builder.
- [static func buildIf<Content>(Content?) -> Content?](./attachmentcontentbuilder/buildif%28_%29.md)
  Provides support for “if” statements in multi-statement closures, producing an optional view that is visible only when the condition evaluates to `true`.
- [static func buildLimitedAvailability(any AttachmentContent) -> some AttachmentContent](./attachmentcontentbuilder/buildlimitedavailability%28_%29.md)
  Provides support for “if” statements with `#available()` clauses in multi-statement closures, producing conditional content for the “then” branch, i.e. the conditionally-available branch.

## See Also

### Attachment types
- [protocol AttachmentContent](./attachmentcontent.md)
  A type that provides content for an attachment content builder.
- [struct TuplePackAttachmentContent](./tuplepackattachmentcontent.md)
- [struct ConditionalAttachmentContent](./conditionalattachmentcontent.md)
- [struct EmptyAttachmentContent](./emptyattachmentcontent.md)
  A attachment content that doesn’t contain any content.
- [struct TupleAttachmentContent](./tupleattachmentcontent.md)
- [struct AnyAttachmentContent](./anyattachmentcontent.md)
  A type-erased attachment content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/attachmentcontentbuilder)*