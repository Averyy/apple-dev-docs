# AppEntityExpectationProviding

**Framework**: App Intents Testing  
**Kind**: protocol  
**Role**: Protocol

A value expectation that checks an app entity’s type and, optionally, its identifier or property values.

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
protocol AppEntityExpectationProviding : IntentValueExpectation
```

## Overview

An entity definition on its own expects any entity of its type. Call [`expect`](./appentitydefinition/expect.md) to also check property values, or [`expectIdentifier(_:)`](./appentitydefinition/expectidentifier%28_%29.md) to expect a specific instance. Use entity expectations to check an intent result, a property that holds an entity, or an entity on its own with [`isSatisfied(by:)`](./intentvalueexpectation/issatisfied%28by%29.md).

You get entity expectations from entity definitions. Don’t declare new conformances to this protocol.

## Relationships

### Inherits From
- [IntentValueExpectation](./intentvalueexpectation.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
### Inherited By
- [ResolvableAppEntityExpectation](./resolvableappentityexpectation.md)
### Conforming Types
- [AppEntityDefinition](./appentitydefinition.md)
- [AppEntityExpectation](./appentityexpectation.md)
- [AppEntityIdentifierExpectation](./appentityidentifierexpectation.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintentstesting/appentityexpectationproviding)*