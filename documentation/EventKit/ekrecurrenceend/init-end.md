# init(end:)

**Framework**: EventKit  
**Kind**: init

Initializes and returns a date-based recurrence end with a given end date.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
convenience init(end endDate: Date)
```

#### Return Value

The initialized recurrence end.

#### Discussion

The end date argument must be a valid `NSDate` and not `nil`; otherwise an exception will be raised.

## Parameters

- `endDate`: The end date.

## See Also

- [Calendar and Reminders Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/DataManagement/Conceptual/EventKitProgGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40009765)
- [convenience init(occurrenceCount: Int)](ekrecurrenceend/init(occurrencecount:).md)
  Initializes and returns a count-based recurrence end with a given maximum occurrence count.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekrecurrenceend/init(end:))*