# dynamicallyCall(withKeywordArguments:)

**Framework**: App Intents Testing  
**Kind**: method  
**Role**: Instance Method

Creates an expectation from value expectations that you label with parameter or property names.

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
func dynamicallyCall(withKeywordArguments args: KeyValuePairs<String, Argument?>) -> Expectation
```

## Return Value

An expectation that checks each labeled parameter or property against its value expectation.

## Discussion

You don’t call this method directly. Swift calls it when you call the callable with labeled arguments. Give every argument a label, and use each label only once; otherwise, the method stops with a precondition failure.

## Parameters

- `args`: The value expectations, keyed by argument label. A `nil` value leaves the corresponding parameter or property unchecked.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintentstesting/intentvalueexpectationcallable/dynamicallycall(withkeywordarguments:))*