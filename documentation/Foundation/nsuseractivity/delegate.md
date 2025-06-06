# delegate

**Framework**: Foundation  
**Kind**: property

The user activity object’s delegate.

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
weak var delegate: (any NSUserActivityDelegate)? { get set }
```

#### Discussion

The user activity delegate is informed when the activity is being saved or continued. For more information on how to implement the delegate, see [`NSUserActivityDelegate`](nsuseractivitydelegate.md).

## See Also

- [protocol NSUserActivityDelegate](nsuseractivitydelegate.md)
  The interface through which a user activity instance notifies its delegate of updates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsuseractivity/delegate)*