# PredicateExpectation

**Framework**: App Intents Testing  
**Kind**: struct  
**Role**: Structure

A value expectation that checks a value of any convertible type against a predicate.

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
struct PredicateExpectation
```

## Overview

Use a predicate expectation for values that aren’t strings, such as numbers, dates, measurements, people, or arrays of these. The predicate’s input can be any type that conforms to `IntentValueConvertible`. A predicate whose input type doesn’t match the value’s type isn’t satisfied.

The predicate’s input type determines how a missing value is handled. A predicate on a non-optional type, like `Predicate<Date>`, isn’t satisfied when the value is missing. A predicate on an optional type, like `Predicate<Date?>`, receives `nil` and decides for itself.

You don’t create a predicate expectation directly. Use [`matches(_:requirement:)`](./intentvalueexpectation/matches%28_,requirement%29.md) instead:

```swift
let createEventIntentDefinition = definitions.intents["CreateEventIntent"]
let expectation = createEventIntentDefinition.expect(
    attendeeCount: .matches(#Predicate<Int> { $0 >= 3 }),
    endDate: .matches(#Predicate<Date?> { $0 == nil || $0! > deadline })
)
```

## Relationships

### Conforms To
- [IntentValueExpectation](./intentvalueexpectation.md)
- [ResolvableIntentValueExpectation](./resolvableintentvalueexpectation.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintentstesting/predicateexpectation)*