# dynamicallyCall(withKeywordArguments:)

**Framework**: App Intents Testing  
**Kind**: method

Returns an instance of `T` by applying the provided argument values to the properties.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
func dynamicallyCall(withKeywordArguments args: KeyValuePairs<String, (any IntentValueExpressing)?>) -> T
```

#### Discussion

Typically, you use this subscript implicitly via function-call syntax, for example:

```swift
let intent = CreateCoffeeIntent.makeIntent(customerName: "MyName", size: 12.0)
```

This is equivalent to the desugared syntax:

```swift
let intent = CreateCoffeeIntent.makeIntent.dynamicallyCall([
    "customerName": "MyName",
    "size": 12.0
])
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintentstesting/intentvaluepropertiescallable/dynamicallycall(withkeywordarguments:))*