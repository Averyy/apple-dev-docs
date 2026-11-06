# AppEntityIdentifierExpectation

**Framework**: App Intents Testing  
**Kind**: struct  
**Role**: Structure

An expectation that checks whether an app entity is a specific instance by comparing its type and identifier.

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
struct AppEntityIdentifierExpectation
```

## Overview

An identifier expectation checks which entity instance a value holds. You can pass it as an intent parameter expectation, as an intent result expectation, or wherever a property holds an entity.

You don’t create an identifier expectation directly. Call [`expectIdentifier(_:)`](./appentitydefinition/expectidentifier%28_%29.md) instead:

```swift
let workCalendarExpectation = createEventIntentDefinition.expect(
    calendar: calendarEntityDefinition.expectIdentifier(
        "edea53fb-90b7-4481-afc7-d86e2dd0d27d"
    )
)
```

To also check the instance’s properties, call `expect` on it, which returns an [`AppEntityExpectation`](./appentityexpectation.md).

## Topics

### Instance Properties
- [var expect: IntentValueExpectationCallable<any IntentValueExpectation, AppEntityExpectation>](./appentityidentifierexpectation/expect.md)
  A callable that creates an entity expectation for the current instance from value expectations for its properties.

## Relationships

### Conforms To
- [AppEntityExpectationProviding](./appentityexpectationproviding.md)
- [IntentValueExpectation](./intentvalueexpectation.md)
- [ResolvableAppEntityExpectation](./resolvableappentityexpectation.md)
- [ResolvableIntentValueExpectation](./resolvableintentvalueexpectation.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintentstesting/appentityidentifierexpectation)*