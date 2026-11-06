# AppIntentExpectationProviding

**Framework**: App Intents Testing  
**Kind**: protocol  
**Role**: Protocol

A type that describes the app intent you expect, including its type and, optionally, its parameter values and result.

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
protocol AppIntentExpectationProviding : Sendable
```

## Overview

An intent definition on its own expects any intent of its type, whatever its parameters are. Call [`expect`](./appintentdefinition/expect.md) to also check parameter values, and [`result(_:)`](./appintentdefinition/result%28_%29.md) or [`result(_:)`](./appintentexpectation/result%28_%29.md) to check the result. Check an intent with [`isSatisfied(by:result:)`](./appintentexpectationproviding/issatisfied%28by,result%29.md), or pass the expectation to a framework that takes intent expectations.

You get intent expectations from intent definitions. Don’t declare new conformances to this protocol.

For example, expect an intent with a title that contains a substring:

```swift
let expectation = createEventIntentDefinition.expect(
    title: .contains("NASA")
)
let isSatisfied = try await expectation.isSatisfied(by: intent)
```

## Topics

### Instance Methods
- [func isSatisfied(by: AnyAppIntent, result: ResolvedIntentResult?) async throws -> Bool](./appintentexpectationproviding/issatisfied%28by,result%29.md)
  Returns a Boolean value that indicates whether an intent and its optional result meet the requirements of the expectation.

## Relationships

### Inherits From
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
### Conforming Types
- [AppIntentDefinition](./appintentdefinition.md)
- [AppIntentExpectation](./appintentexpectation.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintentstesting/appintentexpectationproviding)*