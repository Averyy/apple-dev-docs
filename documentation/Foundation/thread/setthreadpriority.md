# setThreadPriority(_:)

**Framework**: Foundation  
**Kind**: method

Sets the current thread’s priority.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class func setThreadPriority(_ p: Double) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the priority assignment succeeded, [`false`](https://developer.apple.com/documentation/Swift/false) otherwise.

#### Discussion

The priorities in this range are mapped to the operating system’s priority values.

## Parameters

- `p`: The new priority, specified with a floating point number from 0.0 to 1.0, where 1.0 is highest priority.

## See Also

- [var qualityOfService: QualityOfService](thread/qualityofservice.md)
- [enum QualityOfService](qualityofservice.md)
  Constants that indicate the nature and importance of work to the system.
- [class func threadPriority() -> Double](thread/threadpriority.md)
  Returns the current thread’s priority.
- [var threadPriority: Double](thread/threadpriority.md)
  The receiver’s priority


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/thread/setthreadpriority(_:))*