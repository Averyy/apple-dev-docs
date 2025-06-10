# init(_:)

**Framework**: Swift  
**Kind**: init

Automatically opt-in to complex equality semantics if the Executor implements `Equatable`.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
init<E>(_ executor: E) where E : SerialExecutor
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unownedserialexecutor/init(_:)-9jcxo)*