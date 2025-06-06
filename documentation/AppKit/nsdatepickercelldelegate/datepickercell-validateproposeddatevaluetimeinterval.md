# datePickerCell(_:validateProposedDateValue:timeInterval:)

**Framework**: AppKit  
**Kind**: method

The delegate receives this message each time the user attempts to change the receiver’s value, allowing the delegate the opportunity to override the change.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
optional func datePickerCell(_ datePickerCell: NSDatePickerCell, validateProposedDateValue proposedDateValue: AutoreleasingUnsafeMutablePointer<NSDate>, timeInterval proposedTimeInterval: UnsafeMutablePointer<TimeInterval>?)
```

#### Discussion

When returning a new `proposedDateValue`, the `NSDate` instance should be autoreleased, and the `proposedDateValue` should not be released by the delegate.

The `proposedDateValue` and `proposedTimeInterval` are guaranteed to lie between the dates returned by [`minDate`](nsdatepickercell/mindate.md) and [`maxDate`](nsdatepickercell/maxdate.md). If you modify these values, you should ensure that the new values are within the appropriate range.

## Parameters

- `datePickerCell`: The cell that sent the message.
- `proposedDateValue`: On input, contains the proposed new date. The delegate may change this value before returning.
- `proposedTimeInterval`: On input, contains the proposed new time interval. The delegate may change this value before returning.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdatepickercelldelegate/datepickercell(_:validateproposeddatevalue:timeinterval:))*