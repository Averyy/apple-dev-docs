# result(value:dialog:)

**Framework**: Swift  
**Kind**: method

Indicates the `AppIntent` finished performing

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
static func result<Value>(value: Value, dialog: IntentDialog) -> Self where Self == IntentResultContainer<Value, Never, Never, IntentDialog>, Value : _IntentValue
```

## Parameters

- `value`: The value produced by the 
- `dialog`: A custom success dialog


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/never/result(value:dialog:))*