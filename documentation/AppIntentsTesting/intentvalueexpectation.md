# IntentValueExpectation

**Framework**: App Intents Testing  
**Kind**: protocol  
**Role**: Protocol

A type that describes the value you expect for an intent parameter, an app entity property, or an intent result.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst 27.3+ (Beta)
- macOS 27.3+ (Beta)
- tvOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)
- watchOS 27.3+ (Beta)

## Declaration

```swift
protocol IntentValueExpectation : Sendable
```

## Overview

A value expectation states a requirement on a single value, such as a string that contains a substring, or a value that’s absent. Pass value expectations to [`expect`](./appentitydefinition/expect.md) and [`result(_:)`](./appintentdefinition/result%28_%29.md) to build entity and intent expectations, or check a value directly with [`isSatisfied(by:)`](./intentvalueexpectation/issatisfied%28by%29.md). Intent parameters accept only [`ResolvableIntentValueExpectation`](./resolvableintentvalueexpectation.md) values; see [`expect`](./appintentdefinition/expect.md).

You get value expectations from the static members that the framework provides, such as [`contains(_:)`](./intentvalueexpectation/contains%28_%29.md), [`isNil`](./intentvalueexpectation/isnil.md), and [`matches(_:requirement:)`](./intentvalueexpectation/matches%28_,requirement%29.md), and from entity definitions and entity expectations. Don’t declare new conformances to this protocol.

For example, check whether an entity from an intent result has a title that contains a substring:

```swift
let event: AnyAppEntity = try result.value
let expectation = eventEntityDefinition.expect(title: .contains("NASA"))
let isSatisfied = try await expectation.isSatisfied(by: event)
```

## Topics

### Instance Methods
- [func isSatisfied(by: (any IntentValueExpressing)?) async throws -> Bool](./intentvalueexpectation/issatisfied%28by%29.md)
  Returns a Boolean value that indicates whether a value meets the requirements of the expectation.
### Type Properties
- [static var isNil: PrimitiveExpectation](./intentvalueexpectation/isnil.md)
  An expectation that requires a parameter, property, or result to have no value.
- [static var notNil: PrimitiveExpectation](./intentvalueexpectation/notnil.md)
  An expectation that requires a parameter, property, or result to have a value.
### Type Methods
- [static func contains(String) -> Self](./intentvalueexpectation/contains%28_%29.md)
  Creates an expectation that requires the value to be a string that contains a substring.
- [static func contains(regex: String) -> Self](./intentvalueexpectation/contains%28regex%29.md)
  Creates an expectation that requires the value to be a string that contains a match for a regular expression.
- [static func equals(String) -> Self](./intentvalueexpectation/equals%28_%29.md)
  Creates an expectation that requires the value to be a string that equals a specified string.
- [static func matches<Input>(Predicate<Input>, requirement: String?) -> PredicateExpectation](./intentvalueexpectation/matches%28_,requirement%29.md)
  Creates an expectation that requires the value to satisfy a predicate, with an optional description of the check.

## Relationships

### Inherits From
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
### Inherited By
- [AppEntityExpectationProviding](./appentityexpectationproviding.md)
- [ResolvableAppEntityExpectation](./resolvableappentityexpectation.md)
- [ResolvableIntentValueExpectation](./resolvableintentvalueexpectation.md)
### Conforming Types
- [AppEntityDefinition](./appentitydefinition.md)
- [AppEntityExpectation](./appentityexpectation.md)
- [AppEntityIdentifierExpectation](./appentityidentifierexpectation.md)
- [PredicateExpectation](./predicateexpectation.md)
- [PrimitiveExpectation](./primitiveexpectation.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintentstesting/intentvalueexpectation)*