# maxDate

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The maximum date that the picker allows as input.

**Availability**:
- macOS

## Declaration

```swift
var maxDate: Date? { get set }
```

```objc
@property (copy, nullable) NSDate * maxDate;
```

## Discussion

Set this property to `nil` if you want to allow any value for the maximum date.

## See Also

### Date Range Constraints
- [var minDate: Date?](./mindate.md)
  The minimum date that the picker allows as input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdatepickercell/maxdate)*