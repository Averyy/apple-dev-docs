# timeInterval

**Framework**: AppKit  
**Kind**: property

The time interval selected by the date picker.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var timeInterval: TimeInterval { get set }
```

#### Discussion

The time interval that represents the receiver’s date range. The date range begins at the date returned by [`dateValue`](nsdatepicker/datevalue.md). This method returns 0 when the receiver is not in the NSRangeDateMode mode.

## See Also

- [var dateValue: Date](nsdatepicker/datevalue.md)
  The date selected by the date picker.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdatepicker/timeinterval)*