# result(value:opensIntent:)

**Framework**: Swift  
**Kind**: method

Indicates the `AppIntent` finished performing

**Availability**:
- iOS 18.2+
- iPadOS 18.2+
- Mac Catalyst 18.2+
- macOS 15.2+
- tvOS 18.2+
- visionOS 2.2+
- watchOS 11.2+

## Declaration

```swift
static func result<Value>(value: Value, opensIntent: some AppIntent) -> Self where Self == IntentResultContainer<Value, Never, Never, Never>, Value : _IntentValue
```

## Parameters

- `value`: The value produced by the 
- `opensIntent`: An   to shows the result of current intent


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/never/result(value:opensintent:)-7awmd)*