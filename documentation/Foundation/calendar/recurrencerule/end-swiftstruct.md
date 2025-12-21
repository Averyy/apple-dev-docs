# Calendar.RecurrenceRule.End

**Framework**: Foundation  
**Kind**: struct

When a recurring event stops recurring

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 1.0+
- watchOS 11.0+

## Declaration

```swift
struct End
```

## Topics

### Instance Properties
- [var date: Date?](calendar/recurrencerule/end-swift.struct/date.md)
  The latest date when the event may occur This value is set when the struct was initialized with `.afterDate()`
- [var occurrences: Int?](calendar/recurrencerule/end-swift.struct/occurrences.md)
  At most many times the event may occur This value is set when the struct was initialized with `.afterOccurrences()`
### Type Properties
- [static var never: Calendar.RecurrenceRule.End](calendar/recurrencerule/end-swift.struct/never.md)
  The event repeats indefinitely
### Type Methods
- [static func afterDate(Date) -> Calendar.RecurrenceRule.End](calendar/recurrencerule/end-swift.struct/afterdate(_:).md)
  The event stops repeating after a given date
- [static func afterOccurrences(Int) -> Calendar.RecurrenceRule.End](calendar/recurrencerule/end-swift.struct/afteroccurrences(_:).md)
  The event stops repeating after a given number of times

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/calendar/recurrencerule/end-swift.struct)*