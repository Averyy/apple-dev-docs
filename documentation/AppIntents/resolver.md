# Resolver

**Framework**: App Intents  
**Kind**: protocol

An interface to convert a value from one type to a different type.

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
protocol Resolver : Hashable, Sendable
```

## Topics

### Resolving the type
- [func resolve(from: Self.Input, context: IntentParameterContext<Self.Output>) async throws -> Self.Output?](resolver/resolve(from:context:).md)
  Converts the specified value into the expected data type.
- [associatedtype Input : _IntentValue](resolver/input.md)
- [associatedtype Output : _IntentValue](resolver/output.md)
### Managing the resolution process
- [protocol ResolverSpecification](resolverspecification.md)
  An internal type that a resolver uses to convert data values.
- [struct EmptyResolverSpecification](emptyresolverspecification.md)
- [struct StringSearchCriteriaFromStringResolverSpecificification](stringsearchcriteriafromstringresolverspecificification.md)
  An internal type that a resolver uses to convert data values.
- [enum ResolverSpecificationBuilder](resolverspecificationbuilder.md)
  A result builder that declaratively specifies a set of resolvers.
### Type Aliases
- [typealias Context](resolver/context.md)

## Relationships

### Inherits From
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
### Inherited By
- [RangeCheckingResolver](rangecheckingresolver.md)
### Conforming Types
- [AttributedStringFromStringResolver](attributedstringfromstringresolver.md)
- [BoolFromStringResolver](boolfromstringresolver.md)
- [DoubleFromIntResolver](doublefromintresolver.md)
- [DoubleFromStringResolver](doublefromstringresolver.md)
- [DoubleResolver](doubleresolver.md)
- [IntFromDoubleResolver](intfromdoubleresolver.md)
- [IntFromStringResolver](intfromstringresolver.md)
- [IntResolver](intresolver.md)
- [StringFromDoubleResolver](stringfromdoubleresolver.md)
- [StringFromIntResolver](stringfromintresolver.md)
- [StringSearchCriteriaFromStringResolverSpecificification](stringsearchcriteriafromstringresolverspecificification.md)
- [URLFromStringResolver](urlfromstringresolver.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/resolver)*