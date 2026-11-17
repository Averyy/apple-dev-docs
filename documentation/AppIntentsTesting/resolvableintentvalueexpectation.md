# ResolvableIntentValueExpectation

**Framework**: App Intents Testing  
**Kind**: protocol  
**Role**: Protocol

A value expectation that checks a value as the caller passed it, before any query runs.

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
protocol ResolvableIntentValueExpectation : IntentValueExpectation
```

## Overview

Intent parameters hold values as the caller passed them, so [`expect`](./appintentdefinition/expect.md) accepts only expectations that conform to this protocol.

You get resolvable expectations from the framework, such as [`contains(_:)`](./intentvalueexpectation/contains%28_%29.md) and [`isNil`](./intentvalueexpectation/isnil.md). Don’t declare new conformances to this protocol.

## Relationships

### Inherits From
- [IntentValueExpectation](./intentvalueexpectation.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
### Inherited By
- [ResolvableAppEntityExpectation](./resolvableappentityexpectation.md)
### Conforming Types
- [AppEntityDefinition](./appentitydefinition.md)
- [AppEntityIdentifierExpectation](./appentityidentifierexpectation.md)
- [PredicateExpectation](./predicateexpectation.md)
- [PrimitiveExpectation](./primitiveexpectation.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintentstesting/resolvableintentvalueexpectation)*