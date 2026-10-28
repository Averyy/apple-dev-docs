# init(occurrenceCount:)

**Framework**: EventKit  
**Kind**: init  
**Role**: Initializer

Initializes and returns a count-based recurrence end with a given maximum occurrence count.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
convenience init(occurrenceCount: Int)
```

```objc
+ (instancetype) recurrenceEndWithOccurrenceCount:(NSUInteger) occurrenceCount;
```

## Return Value

The initialized recurrence end.

## Discussion

The maximum occurrence count argument must be a positive integer and not `0`; otherwise an exception will be raised.

## Parameters

- `occurrenceCount`: The maximum occurrence count.

## See Also

### Creating a Recurrence End
- [convenience init(end: Date)](./init%28end%29.md)
  Initializes and returns a date-based recurrence end with a given end date.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekrecurrenceend/init(occurrencecount:))*