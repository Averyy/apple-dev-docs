# maxDate

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The date picker’s maximum date value.

**Availability**:
- macOS

## Declaration

```swift
var maxDate: Date? { get set }
```

```objc
@property (copy, nullable) NSDate * maxDate;
```

#### Discussion

This property represents the maximum value that the date picker allows as input. `nil` indicates no maximum date.

## See Also

### Constraining the Displayable/Selectable Range
- [var minDate: Date?](./mindate.md)
  The date picker’s minimum date value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdatepicker/maxdate)*