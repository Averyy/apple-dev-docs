# executor

**Framework**: Swift  
**Kind**: property

The main executor, which is started implicitly by the `async main` entry point and owns the “main” thread.

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
static var executor: any MainExecutor { get }
```

#### Discussion

Attempting to set this after the first `enqueue` on the main executor is a fatal error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/mainactor/executor)*