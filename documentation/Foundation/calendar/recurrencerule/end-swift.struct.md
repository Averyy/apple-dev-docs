# Calendar.RecurrenceRule.End

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

When a recurring event stops recurring.

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
- [var date: Date?](./end-swift.struct/date.md)
  The latest date when the event may occur This value is set when the struct was initialized with `.afterDate()`
- [var occurrences: Int?](./end-swift.struct/occurrences.md)
  At most many times the event may occur This value is set when the struct was initialized with `.afterOccurrences()`
### Type Properties
- [static var never: Calendar.RecurrenceRule.End](./end-swift.struct/never.md)
  The event repeats indefinitely
### Type Methods
- [static func afterDate(Date) -> Calendar.RecurrenceRule.End](./end-swift.struct/afterdate%28_%29.md)
  The event stops repeating after a given date
- [static func afterOccurrences(Int) -> Calendar.RecurrenceRule.End](./end-swift.struct/afteroccurrences%28_%29.md)
  The event stops repeating after a given number of times

## Relationships

### Conforms To
- [Copyable](../../../Swift/copyable.md)
- [CustomStringConvertible](../../../Swift/customstringconvertible.md)
- [Decodable](../../../Swift/decodable.md)
- [Encodable](../../../Swift/encodable.md)
- [Equatable](../../../Swift/equatable.md)
- [Escapable](../../../Swift/escapable.md)
- [Hashable](../../../Swift/hashable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/calendar/recurrencerule/end-swift.struct)*