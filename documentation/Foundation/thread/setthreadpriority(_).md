# setThreadPriority(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

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

```objc
+ (BOOL) setThreadPriority:(double) p;
```

#### Return Value

[`true`](../../Swift/true.md) if the priority assignment succeeded, [`false`](../../Swift/false.md) otherwise.

#### Discussion

The priorities in this range are mapped to the operating system’s priority values.

## Parameters

- `p`: The new priority, specified with a floating point number from 0.0 to 1.0, where 1.0 is highest priority.

## See Also

### Prioritizing Thread Work
- [var qualityOfService: QualityOfService](./qualityofservice.md)
- [enum QualityOfService](../qualityofservice.md)
  Constants that indicate the nature and importance of work to the system.
- [class func threadPriority() -> Double](./threadpriority%28%29.md)
  Returns the current thread’s priority.
- [var threadPriority: Double](./threadpriority.md)
  The receiver’s priority


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/thread/setthreadpriority(_:))*