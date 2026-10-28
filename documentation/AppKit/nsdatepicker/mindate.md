# minDate

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The date picker’s minimum date value.

**Availability**:
- macOS

## Declaration

```swift
var minDate: Date? { get set }
```

```objc
@property (copy, nullable) NSDate * minDate;
```

## Discussion

This property represents the minimum value that the date picker allows as input. `nil` indicates no minimum date.

## See Also

### Constraining the Displayable/Selectable Range
- [var maxDate: Date?](./maxdate.md)
  The date picker’s maximum date value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdatepicker/mindate)*