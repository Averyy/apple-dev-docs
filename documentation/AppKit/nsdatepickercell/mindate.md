# minDate

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The minimum date that the picker allows as input.

**Availability**:
- macOS

## Declaration

```swift
var minDate: Date? { get set }
```

```objc
@property (copy, nullable) NSDate * minDate;
```

#### Discussion

Set this property to `nil` if you want to allow any value for the minimum date.

## See Also

### Date Range Constraints
- [var maxDate: Date?](./maxdate.md)
  The maximum date that the picker allows as input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdatepickercell/mindate)*