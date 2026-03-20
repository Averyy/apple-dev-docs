# init(_:)

**Framework**: Swift  
**Kind**: init

Automatically opt-in to complex equality semantics if the Executor implements `Equatable`.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+
- macOS 26.4+
- tvOS 26.4+
- visionOS 26.4+
- watchOS 26.4+

## Declaration

```swift
init<E>(_ executor: E) where E : SerialExecutor
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unownedserialexecutor/init(_:)-9jcxo)*