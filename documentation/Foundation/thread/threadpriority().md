# threadPriority()

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Returns the current thread’s priority.

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
class func threadPriority() -> Double
```

```objc
+ (double) threadPriority;
```

## Return Value

The current thread’s priority, which is specified by a floating point number from 0.0 to 1.0, where 1.0 is highest priority.

## Discussion

The priorities in this range are mapped to the operating system’s priority values. A “typical” thread priority might be 0.5, but because the priority is determined by the kernel, there is no guarantee what this value actually will be.

## See Also

### Prioritizing Thread Work
- [var qualityOfService: QualityOfService](./qualityofservice.md)
- [enum QualityOfService](../qualityofservice.md)
  Constants that indicate the nature and importance of work to the system.
- [var threadPriority: Double](./threadpriority.md)
  The receiver’s priority
- [class func setThreadPriority(Double) -> Bool](./setthreadpriority%28_%29.md)
  Sets the current thread’s priority.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/thread/threadpriority())*