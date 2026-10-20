# isEqual(to:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean value that indicates whether a given object is a date that is exactly equal the receiver.

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
func isEqual(to otherDate: Date) -> Bool
```

```objc
- (BOOL) isEqualToDate:(NSDate *) otherDate;
```

#### Return Value

[`true`](../../Swift/true.md) if the `otherDate` is an [`NSDate`](../nsdate.md) object and is exactly equal to the receiver, otherwise [`false`](../../Swift/false.md).

#### Discussion

This method detects sub-second differences between dates. If you want to compare dates with a less fine granularity, use [`timeIntervalSince(_:)`](./timeintervalsince%28_%29.md) to compare the two dates.

## Parameters

- `otherDate`: The date to compare with the receiver.

## See Also

### Related Documentation
- [func isEqual(Any?) -> Bool](../../ObjectiveC/nsobjectprotocol/isequal%28_%29.md)
  Returns a Boolean value that indicates whether the receiver and a given object are equal.
### Comparing Dates
- [func earlierDate(Date) -> Date](./earlierdate%28_%29.md)
  Returns the earlier of the receiver and another given date.
- [func laterDate(Date) -> Date](./laterdate%28_%29.md)
  Returns the later of the receiver and another given date.
- [func compare(Date) -> ComparisonResult](./compare%28_%29.md)
  Indicates the temporal ordering of the receiver and another given date.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdate/isequal(to:))*