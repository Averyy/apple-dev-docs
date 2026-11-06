# AppEntityExpectation

**Framework**: App Intents Testing  
**Kind**: struct  
**Role**: Structure

An expectation that checks an app entity’s type, its property values, and, optionally, its instance identifier.

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
struct AppEntityExpectation
```

## Overview

An entity expectation checks an entity’s properties, such as those of an entity that an intent returns. It checks each property independently, and doesn’t check properties that have no expectation.

You don’t create an entity expectation directly. Call `expect` on an [`AppEntityDefinition`](./appentitydefinition.md) to check an entity’s properties, or on an [`AppEntityIdentifierExpectation`](./appentityidentifierexpectation.md) to also check its identifier:

```swift
let expectation = createEventIntentDefinition.result(
    eventEntityDefinition.expect(
        title: .contains("NASA"),
        endDate: .isNil
    )
)
```

Pass an entity expectation to an intent’s result expectation, or wherever a property holds an entity. Intent parameters don’t accept entity expectations, because parameters hold entities as the caller passed them, before any entity query runs, so their properties aren’t available. To check an entity on its own, call [`isSatisfied(by:)`](./intentvalueexpectation/issatisfied%28by%29.md).

## Relationships

### Conforms To
- [AppEntityExpectationProviding](./appentityexpectationproviding.md)
- [IntentValueExpectation](./intentvalueexpectation.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintentstesting/appentityexpectation)*