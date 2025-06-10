# result(opensIntent:)

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
static func result<OpensAppIntent>(opensIntent: OpensAppIntent) -> Self where Self == IntentResultContainer<Never, OpensAppIntent, Never, Never>, OpensAppIntent : AppIntent
```

## Parameters

- `opensIntent`: An   to shows the result of current intent


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/never/result(opensintent:)-6dbqd)*