# NSDatePicker.Mode

**Framework**: AppKit  
**Kind**: enum  
**Role**: Enumeration

Constants that define whether the picker provides a single date, or a range of dates.

**Availability**:
- macOS

## Declaration

```swift
enum Mode
```

```c
enum NSDatePickerMode : NSUInteger;
```

## Topics

### Enumeration Cases
- [NSDatePicker.Mode.range](./mode/range.md)
- [NSDatePicker.Mode.single](./mode/single.md)
### Initializers
- [init?(rawValue: UInt)](./mode/init%28rawvalue%29.md)
### Constants
- [NSSingleDateMode](../nssingledatemode.md)
- [NSRangeDateMode](../nsrangedatemode.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Controlling Date Picker Range and Mode
- [var calendar: Calendar?](./calendar.md)
  The calendar used by the date picker.
- [var locale: Locale?](./locale.md)
  The date picker’s locale.
- [var datePickerMode: NSDatePicker.Mode](./datepickermode.md)
  The date picker’s mode.
- [var timeZone: TimeZone?](./timezone.md)
  The time zone for the date picker.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdatepicker/mode)*