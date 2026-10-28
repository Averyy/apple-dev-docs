# earlierDate(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns the earlier of the receiver and another given date.

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
func earlierDate(_ anotherDate: Date) -> Date
```

```objc
- (NSDate *) earlierDate:(NSDate *) anotherDate;
```

## Return Value

The earlier of the receiver and `anotherDate`, determined using [`timeIntervalSince(_:)`](./timeintervalsince%28_%29.md). If the receiver and `anotherDate` represent the same date, returns the receiver.

## Parameters

- `anotherDate`: The date with which to compare the receiver.

## See Also

### Related Documentation
- [func isEqual(Any?) -> Bool](../../ObjectiveC/nsobjectprotocol/isequal%28_%29.md)
  Returns a Boolean value that indicates whether the receiver and a given object are equal.
### Comparing Dates
- [func isEqual(to: Date) -> Bool](./isequal%28to%29.md)
  Returns a Boolean value that indicates whether a given object is a date that is exactly equal the receiver.
- [func laterDate(Date) -> Date](./laterdate%28_%29.md)
  Returns the later of the receiver and another given date.
- [func compare(Date) -> ComparisonResult](./compare%28_%29.md)
  Indicates the temporal ordering of the receiver and another given date.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdate/earlierdate(_:))*