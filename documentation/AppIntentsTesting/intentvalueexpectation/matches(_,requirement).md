# matches(_:requirement:)

**Framework**: App Intents Testing  
**Kind**: method  
**Role**: Type Method

Creates an expectation that requires the value to satisfy a predicate, with an optional description of the check.

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
static func matches<Input>(_ predicate: Predicate<Input>, requirement: String? = nil) -> PredicateExpectation where Input : IntentValueConvertible
```

Available when `Self` is `PredicateExpectation`.

## Return Value

A predicate expectation that evaluates `predicate` against the value.

## Discussion

Use this method for values that aren’t strings. A predicate on a non-optional type isn’t satisfied when the value is missing, and a predicate on an optional type receives `nil` and decides for itself. A predicate whose input type doesn’t match the value’s type isn’t satisfied.

## Parameters

- `predicate`: The predicate to evaluate against the value.
- `requirement`: A readable description of the check. The default is `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintentstesting/intentvalueexpectation/matches(_:requirement:))*