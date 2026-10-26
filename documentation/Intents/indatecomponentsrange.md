# INDateComponentsRange

**Framework**: Intents  
**Kind**: class  
**Role**: Class

A span of time.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
class INDateComponentsRange
```

```objc
@interface INDateComponentsRange : NSObject
```

#### Overview

Use an [`INDateComponentsRange`](./indatecomponentsrange.md) object to specify date- or time-related information when responding to an intent. For example, a ride service might use this object to specify possible pickup times for the user.

You create date components range objects when providing a response that includes a time span. Use this object to specify a range of times to include in the corresponding response. When displaying the date range information to the user, Siri or Maps formats the information appropriately.

## Topics

### Initializing a Date Components Range
- [convenience init(start: DateComponents?, end: DateComponents?)](./indatecomponentsrange/init%28start,end%29.md)
  Initializes the object using the specified start and end dates.
- [init(start: DateComponents?, end: DateComponents?, recurrenceRule: INRecurrenceRule?)](./indatecomponentsrange/init%28start,end,recurrencerule%29.md)
  Initializes the date range to a repeating time period.
- [convenience init(ekRecurrenceRule: EKRecurrenceRule)](./indatecomponentsrange/init%28ekrecurrencerule%29-5p7kt.md)
  Initializes the date range using the specified recurrence rule.
### Getting the Date Information
- [var startDateComponents: DateComponents?](./indatecomponentsrange/startdatecomponents.md)
  The start date of the range.
- [var endDateComponents: DateComponents?](./indatecomponentsrange/enddatecomponents.md)
  The end date of the range.
### Getting Recurring Date Information
- [var recurrenceRule: INRecurrenceRule?](./indatecomponentsrange/recurrencerule.md)
  The rule for repeating the date range.
- [func ekRecurrenceRule() -> EKRecurrenceRule?](./indatecomponentsrange/ekrecurrencerule%28%29.md)
  Returns an Event Kit recurrence rule that matches the available information.
### Initializers
- [convenience init(EKRecurrenceRule: EKRecurrenceRule)](./indatecomponentsrange/init%28ekrecurrencerule%29-n8xm.md)
- [init?(coder: NSCoder)](./indatecomponentsrange/init%28coder%29.md)
- [convenience init(startDateComponents: DateComponents?, endDateComponents: DateComponents?)](./indatecomponentsrange/init%28startdatecomponents,enddatecomponents%29.md)
- [init(startDateComponents: DateComponents?, endDateComponents: DateComponents?, recurrenceRule: INRecurrenceRule?)](./indatecomponentsrange/init%28startdatecomponents,enddatecomponents,recurrencerule%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Date
- [class INRecurrenceRule](./inrecurrencerule.md)
  An object that describes the pattern to use when repeating an event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/indatecomponentsrange)*