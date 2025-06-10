# earliestBeginDate

**Framework**: Background Tasks  
**Kind**: property

The earliest date and time at which to run the task.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var earliestBeginDate: Date? { get set }
```

#### Discussion

Specify `nil` for no start delay.

Setting the property indicates that the background task shouldn’t start any earlier than this date. However, the system doesn’t guarantee launching the task at the specified date, but only that it won’t begin sooner.

## See Also

- [var identifier: String](bgtaskrequest/identifier.md)
  The identifier of the task associated with the request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundtasks/bgtaskrequest/earliestbegindate)*