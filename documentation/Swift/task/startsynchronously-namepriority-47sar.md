# startSynchronously(name:priority:_:)

**Framework**: Swift  
**Kind**: method

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)
- Unknown ?+ - Deprecated
- tvOS 26.0+ (Beta)

## Declaration

```swift
@discardableResult
static func startSynchronously(name: String? = nil, priority: TaskPriority? = nil, _ operation: @escaping @isolated(any) () async throws -> Success) -> Task<Success, any Error>
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/task/startsynchronously(name:priority:_:)-47sar)*