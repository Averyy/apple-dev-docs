# NSDatePickerCellDelegate

**Framework**: AppKit  
**Kind**: protocol

A set of optional methods implemented by delegates of [`NSDatePickerCell`](nsdatepickercell.md) objects.

**Availability**:
- macOS ?+

## Declaration

```swift
protocol NSDatePickerCellDelegate : NSObjectProtocol
```

## Topics

### Content Validation
- [func datePickerCell(NSDatePickerCell, validateProposedDateValue: AutoreleasingUnsafeMutablePointer<NSDate>, timeInterval: UnsafeMutablePointer<TimeInterval>?)](nsdatepickercelldelegate/datepickercell(_:validateproposeddatevalue:timeinterval:).md)
  The delegate receives this message each time the user attempts to change the receiver’s value, allowing the delegate the opportunity to override the change.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class NSDatePickerCell](nsdatepickercell.md)
  An object that controls the behavior of a date picker, or of a single date picker cell in a matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdatepickercelldelegate)*