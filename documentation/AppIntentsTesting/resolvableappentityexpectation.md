# ResolvableAppEntityExpectation

**Framework**: App Intents Testing  
**Kind**: protocol  
**Role**: Protocol

An entity expectation that checks an app entity as the caller passed it, before any query runs.

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
protocol ResolvableAppEntityExpectation : AppEntityExpectationProviding, ResolvableIntentValueExpectation
```

## Overview

No query runs to populate the entity parameters of an intent, so an entity parameter accepts only an expectation that conforms to this protocol, such as an [`AppEntityDefinition`](./appentitydefinition.md) that checks the entity’s type or an [`AppEntityIdentifierExpectation`](./appentityidentifierexpectation.md) that checks its identifier. An [`AppEntityExpectation`](./appentityexpectation.md), which checks property values, doesn’t conform.

You get resolvable entity expectations from entity definitions. Don’t declare new conformances to this protocol.

## Relationships

### Inherits From
- [AppEntityExpectationProviding](./appentityexpectationproviding.md)
- [IntentValueExpectation](./intentvalueexpectation.md)
- [ResolvableIntentValueExpectation](./resolvableintentvalueexpectation.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
### Conforming Types
- [AppEntityDefinition](./appentitydefinition.md)
- [AppEntityIdentifierExpectation](./appentityidentifierexpectation.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintentstesting/resolvableappentityexpectation)*