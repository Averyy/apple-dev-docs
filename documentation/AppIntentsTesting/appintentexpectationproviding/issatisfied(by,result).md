# isSatisfied(by:result:)

**Framework**: App Intents Testing  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean value that indicates whether an intent and its optional result meet the requirements of the expectation.

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
func isSatisfied(by intent: AnyAppIntent, result: ResolvedIntentResult? = nil) async throws -> Bool
```

## Return Value

`true` if the intent and its result satisfy the expectation; otherwise, `false`.

## Discussion

Use this method to check an intent, and the result you get from performing it, against the expectation. Checking an expectation doesn’t perform the intent. The method checks each parameter independently; a parameter that the method can’t evaluate, such as a value of the wrong type, isn’t satisfied and doesn’t stop the method from checking the others.

## Parameters

- `intent`: The intent to check.
- `result`: The result of performing the intent. If you omit this argument, the method treats the intent’s result as absent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintentstesting/appintentexpectationproviding/issatisfied(by:result:))*