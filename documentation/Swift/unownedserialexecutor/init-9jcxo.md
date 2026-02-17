# init(_:)

**Framework**: Swift  
**Kind**: init

Automatically opt-in to complex equality semantics if the Executor implements `Equatable`.

**Availability**:
- iOS 26.4+ (Beta)
- iPadOS 26.4+ (Beta)
- Mac Catalyst 26.4+ (Beta)
- macOS 26.4+ (Beta)
- tvOS 26.4+ (Beta)
- visionOS 26.4+ (Beta)
- watchOS 26.4+ (Beta)

## Declaration

```swift
init<E>(_ executor: E) where E : SerialExecutor
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unownedserialexecutor/init(_:)-9jcxo)*