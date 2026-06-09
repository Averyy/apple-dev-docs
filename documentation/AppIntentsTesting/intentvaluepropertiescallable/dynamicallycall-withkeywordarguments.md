# dynamicallyCall(withKeywordArguments:)

**Framework**: App Intents Testing  
**Kind**: method

Returns an instance of `T` by applying the provided argument values to the properties.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

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