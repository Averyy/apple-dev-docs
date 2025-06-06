# isComplete

**Framework**: CallKit  
**Kind**: property

A Boolean value that indicates whether the action has been performed by the provider.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
var isComplete: Bool { get }
```

#### Discussion

This property is initialized to [`false`](https://developer.apple.com/documentation/swift/false), and is set to [`true`](https://developer.apple.com/documentation/swift/true) when either the [`fulfill()`](cxaction/fulfill().md) or [`fail()`](cxaction/fail().md) method is called.

#### See Also

##### Related Documentation

- [`fulfill()`](cxaction/fulfill().md)
- [`fail()`](cxaction/fail().md)

## See Also

- [var uuid: UUID](cxaction/uuid.md)
  The unique identifier for the action.
- [var timeoutDate: Date](cxaction/timeoutdate.md)
  The time after which the action cannot be completed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxaction/iscomplete)*