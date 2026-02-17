# asSchedulingExecutor

**Framework**: Swift  
**Kind**: property  
**Required**: Yes

Return this executable as a SchedulingExecutor, or nil if that is unsupported.

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
var asSchedulingExecutor: (any SchedulingExecutor)? { get }
```

#### Discussion

Executors that implement SchedulingExecutor should provide their own copy of this method, which will allow the compiler to avoid a potentially expensive runtime cast.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/executor/asschedulingexecutor)*