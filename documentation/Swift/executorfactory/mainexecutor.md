# mainExecutor

**Framework**: Swift  
**Kind**: property  
**Required**: Yes

Constructs and returns the main executor, which is started implicitly by the `async main` entry point and owns the “main” thread.

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
static var mainExecutor: any MainExecutor { get }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/executorfactory/mainexecutor)*