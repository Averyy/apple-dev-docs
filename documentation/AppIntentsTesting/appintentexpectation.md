# AppIntentExpectation

**Framework**: App Intents Testing  
**Kind**: struct  
**Role**: Structure

An expectation that checks an app intent’s parameters and, optionally, the result the intent returns.

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
struct AppIntentExpectation
```

## Overview

Use an app intent expectation to declare what you expect of an intent before you have one, then check an intent against it or pass it to a framework that takes intent expectations. The expectation checks only the parameters you specify, and checks the result only when you add a result expectation. Checking an expectation doesn’t perform the intent.

You don’t create an app intent expectation directly. Call [`expect`](./appintentdefinition/expect.md) or [`result(_:)`](./appintentdefinition/result%28_%29.md) on an intent definition, and optionally call [`result(_:)`](./appintentexpectation/result%28_%29.md) to add an expectation on the result. To check an intent and its result, call [`isSatisfied(by:result:)`](./appintentexpectationproviding/issatisfied%28by,result%29.md):

```swift
let expectation = createEventIntentDefinition
    .expect(title: .contains("NASA"))
    .result(eventEntityDefinition)

let result = try await intent.run()
let isSatisfied = try await expectation.isSatisfied(
    by: intent,
    result: result
)
```

## Topics

### Instance Methods
- [func result((any IntentValueExpectation)?) -> AppIntentExpectation](./appintentexpectation/result%28_%29.md)
  Returns an intent expectation that also requires the intent’s result to satisfy the value expectation you specify.

## Relationships

### Conforms To
- [AppIntentExpectationProviding](./appintentexpectationproviding.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintentstesting/appintentexpectation)*