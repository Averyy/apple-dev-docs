# init(_:)

**Framework**: Swift  
**Kind**: init

Automatically opt-in to complex equality semantics if the Executor implements `Equatable`.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
init<E>(_ executor: E) where E : SerialExecutor
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unownedserialexecutor/init(_:)-9jcxo)*