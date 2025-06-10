# currentSchedulableExecutor

**Framework**: Swift  
**Kind**: property

Get the current  executor, if any.

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
static var currentSchedulableExecutor: (any SchedulableExecutor)? { get }
```

#### Discussion

This follows the same logic as `currentExecutor`, except that it ignores any executor that isn’t a `SchedulableExecutor`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/task/currentschedulableexecutor)*