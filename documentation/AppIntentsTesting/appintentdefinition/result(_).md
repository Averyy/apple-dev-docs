# result(_:)

**Framework**: App Intents Testing  
**Kind**: method  
**Role**: Instance Method

Creates an intent expectation that checks the result the intent returns, but none of its parameters.

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
func result(_ resultExpectation: any IntentValueExpectation) -> AppIntentExpectation
```

## Return Value

An intent expectation that checks only the intent’s result.

## Discussion

To check the result, perform the intent and pass both the intent and its result to [`isSatisfied(by:result:)`](../appintentexpectationproviding/issatisfied%28by,result%29.md). If you omit the result, the framework treats the intent as returning no value. For example:

```swift
let createEventIntentDefinition = definitions.intents["CreateEventIntent"]
let intent = createEventIntentDefinition.makeIntent(title: "NASA launch")
let result = try await intent.run()

let expectation = createEventIntentDefinition.result(.notNil)
let isSatisfied = try await expectation.isSatisfied(
    by: intent,
    result: result
)
```

## Parameters

- `resultExpectation`: The value expectation for the intent’s result, such as an [`AppEntityExpectation`](../appentityexpectation.md). Pass [`isNil`](../intentvalueexpectation/isnil.md) to expect no result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintentstesting/appintentdefinition/result(_:))*