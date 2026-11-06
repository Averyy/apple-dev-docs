# isSatisfied(by:)

**Framework**: App Intents Testing  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean value that indicates whether a value meets the requirements of the expectation.

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
func isSatisfied(by value: (any IntentValueExpressing)?) async throws -> Bool
```

## Return Value

`true` if the value satisfies the expectation; otherwise, `false`.

## Discussion

Use this method to check an intent parameter value, an app entity property value, an intent result value, or an entity on its own. For an entity, the method checks each property independently; a property that the method can’t evaluate, such as a value of the wrong type, isn’t satisfied and doesn’t stop the method from checking the others.

## Parameters

- `value`: The value to check, or `nil` for an absent value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintentstesting/intentvalueexpectation/issatisfied(by:))*