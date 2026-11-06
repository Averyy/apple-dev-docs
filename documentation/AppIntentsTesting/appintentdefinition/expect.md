# expect

**Framework**: App Intents Testing  
**Kind**: property  
**Role**: Instance Property

A callable that creates an intent expectation from value expectations for the intent’s parameters.

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
var expect: IntentValueExpectationCallable<any ResolvableIntentValueExpectation, AppIntentExpectation> { get }
```

## Discussion

Call `expect` with a labeled argument for each parameter you want to check. Each label names a parameter, and each argument is the value expectation for it. The order of the labels doesn’t matter. The expectation doesn’t check parameters you omit or pass `nil` for. Pass [`isNil`](../intentvalueexpectation/isnil.md) to expect a parameter to be absent. For example:

```swift
let createEventIntentDefinition = definitions.intents["CreateEventIntent"]
let expectation = createEventIntentDefinition.expect(
    title: .contains("NASA")
)
```

The framework checks each parameter as the caller passed it, before any entity query runs. An entity parameter accepts an entity definition or an [`AppEntityIdentifierExpectation`](../appentityidentifierexpectation.md), but not an [`AppEntityExpectation`](../appentityexpectation.md).

The framework matches labels to parameter names when it evaluates the expectation, not when your code compiles, so a misspelled label reads as a missing parameter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintentstesting/appintentdefinition/expect)*