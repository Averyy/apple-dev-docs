# IntentValueExpectationCallable

**Framework**: App Intents Testing  
**Kind**: struct  
**Role**: Structure

A value that you call with labeled value expectations to create an expectation on the corresponding parameters or properties.

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
@dynamicCallable
struct IntentValueExpectationCallable<Argument, Expectation> where Argument : Sendable
```

## Overview

A callable lets you write an expectation as a single call, where each argument label names a parameter or property and each argument is the value expectation for it. The callable’s argument type determines which value expectations the arguments accept, and its expectation type is the expectation the call creates.

You don’t create a callable directly. Get one from the `expect` property of a definition, such as [`expect`](./appintentdefinition/expect.md) or [`expect`](./appentitydefinition/expect.md), and call it like a method:

```swift
let createEventIntentDefinition = definitions.intents["CreateEventIntent"]
let expectation = createEventIntentDefinition.expect(
    title: .contains("NASA")
)
```

## Topics

### Instance Methods
- [func dynamicallyCall(withKeywordArguments: KeyValuePairs<String, Argument?>) -> Expectation](./intentvalueexpectationcallable/dynamicallycall%28withkeywordarguments%29.md)
  Creates an expectation from value expectations that you label with parameter or property names.

## Relationships

### Conforms To
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintentstesting/intentvalueexpectationcallable)*