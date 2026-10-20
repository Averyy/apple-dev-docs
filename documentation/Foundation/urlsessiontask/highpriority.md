# highPriority

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

A high URL session task priority, with a floating point value above the default value and below the maximum of `1.0`.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class let highPriority: Float
```

```c
extern const float NSURLSessionTaskPriorityHigh;
```

## See Also

### Priority constants
- [class let defaultPriority: Float](./defaultpriority.md)
  The default URL session task priority, used implicitly for any task you have not prioritized.
- [class let lowPriority: Float](./lowpriority.md)
  A low URL session task priority, with a floating point value above the minimum of `0` and below the default value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsessiontask/highpriority)*