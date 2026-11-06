# result(_:)

**Framework**: App Intents Testing  
**Kind**: method  
**Role**: Instance Method

Returns an intent expectation that also requires the intent’s result to satisfy the value expectation you specify.

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
func result(_ resultExpectation: (any IntentValueExpectation)?) -> AppIntentExpectation
```

## Return Value

An intent expectation that checks the same parameters and uses `resultExpectation` for the result, replacing any earlier result expectation.

## Discussion

Call this method after [`expect`](../appintentdefinition/expect.md) to check an intent’s parameters and its result together:

```swift
let expectation = createEventIntentDefinition
    .expect(title: .contains("NASA"))
    .result(eventEntityDefinition)
```

## Parameters

- `resultExpectation`: The value expectation for the intent’s result. Pass [`isNil`](../intentvalueexpectation/isnil.md) to expect no result, or `nil` to leave the result unchecked.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintentstesting/appintentexpectation/result(_:))*