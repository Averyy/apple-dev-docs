# ResolverSpecificationBuilder

**Framework**: App Intents  
**Kind**: enum

A result builder that declaratively specifies a set of resolvers.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
@resultBuilder
enum ResolverSpecificationBuilder<Property> where Property : _IntentValue
```

## Topics

### Building the resolver specification
- [static func buildBlock() -> some ResolverSpecification](resolverspecificationbuilder/buildblock.md)
- [static func buildBlock<R0>(R0) -> some ResolverSpecification](resolverspecificationbuilder/buildblock(_:).md)
- [static func buildBlock<R0, R1>(R0, R1) -> some ResolverSpecification](resolverspecificationbuilder/buildblock(_:_:).md)
- [static func buildBlock<R0, R1, R2>(R0, R1, R2) -> some ResolverSpecification](resolverspecificationbuilder/buildblock(_:_:_:).md)
- [static func buildBlock<R0, R1, R2, R3>(R0, R1, R2, R3) -> some ResolverSpecification](resolverspecificationbuilder/buildblock(_:_:_:_:).md)
- [static func buildBlock<R0, R1, R2, R3, R4>(R0, R1, R2, R3, R4) -> some ResolverSpecification](resolverspecificationbuilder/buildblock(_:_:_:_:_:).md)
- [static func buildBlock<R0, R1, R2, R3, R4, R5>(R0, R1, R2, R3, R4, R5) -> some ResolverSpecification](resolverspecificationbuilder/buildblock(_:_:_:_:_:_:).md)
- [static func buildBlock<R0, R1, R2, R3, R4, R5, R6>(R0, R1, R2, R3, R4, R5, R6) -> some ResolverSpecification](resolverspecificationbuilder/buildblock(_:_:_:_:_:_:_:).md)
- [static func buildBlock<R0, R1, R2, R3, R4, R5, R6, R7>(R0, R1, R2, R3, R4, R5, R6, R7) -> some ResolverSpecification](resolverspecificationbuilder/buildblock(_:_:_:_:_:_:_:_:).md)
- [static func buildBlock<R0, R1, R2, R3, R4, R5, R6, R7, R8>(R0, R1, R2, R3, R4, R5, R6, R7, R8) -> some ResolverSpecification](resolverspecificationbuilder/buildblock(_:_:_:_:_:_:_:_:_:).md)
### Structures
- [ResolverSpecificationBuilder.Specification](resolverspecificationbuilder/specification.md)
### Type Methods
- [static func buildBlock<R0, R1, R2, R3, R4, R5, R6, R7, R8, R9>(R0, R1, R2, R3, R4, R5, R6, R7, R8, R9) -> some ResolverSpecification](resolverspecificationbuilder/buildblock(_:_:_:_:_:_:_:_:_:_:).md)
- [static func buildBlock<R0, R1, R2, R3, R4, R5, R6, R7, R8, R9, R10>(R0, R1, R2, R3, R4, R5, R6, R7, R8, R9, R10) -> some ResolverSpecification](resolverspecificationbuilder/buildblock(_:_:_:_:_:_:_:_:_:_:_:).md)
- [static func buildBlock<R0, R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11>(R0, R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11) -> some ResolverSpecification](resolverspecificationbuilder/buildblock(_:_:_:_:_:_:_:_:_:_:_:_:).md)
- [static func buildBlock<R0, R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, R12>(R0, R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, R12) -> some ResolverSpecification](resolverspecificationbuilder/buildblock(_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
- [static func buildBlock<R0, R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, R12, R13>(R0, R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, R12, R13) -> some ResolverSpecification](resolverspecificationbuilder/buildblock(_:_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
- [static func buildBlock<R0, R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, R12, R13, R14>(R0, R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, R12, R13, R14) -> some ResolverSpecification](resolverspecificationbuilder/buildblock(_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
- [static func buildExpression<ResolverType>(ResolverType) -> ResolverType](resolverspecificationbuilder/buildexpression(_:).md)
- [static func buildPartialBlock<each Accumulated, R>(accumulated: ResolverSpecificationBuilder<Property>.Specification<Property, repeat each Accumulated>, next: R) -> ResolverSpecificationBuilder<Property>.Specification<Property, repeat each Accumulated, R>](resolverspecificationbuilder/buildpartialblock(accumulated:next:).md)
- [static func buildPartialBlock<R>(first: R) -> ResolverSpecificationBuilder<Property>.Specification<Property, R>](resolverspecificationbuilder/buildpartialblock(first:).md)

## See Also

- [protocol ResolverSpecification](resolverspecification.md)
  An internal type that a resolver uses to convert data values.
- [struct EmptyResolverSpecification](emptyresolverspecification.md)
- [struct StringSearchCriteriaFromStringResolverSpecificification](stringsearchcriteriafromstringresolverspecificification.md)
  An internal type that a resolver uses to convert data values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/resolverspecificationbuilder)*