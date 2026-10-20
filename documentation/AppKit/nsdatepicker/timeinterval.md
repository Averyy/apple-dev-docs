# timeInterval

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The time interval selected by the date picker.

**Availability**:
- macOS

## Declaration

```swift
var timeInterval: TimeInterval { get set }
```

```objc
@property NSTimeInterval timeInterval;
```

#### Discussion

The time interval that represents the receiver’s date range. The date range begins at the date returned by [`dateValue`](./datevalue.md). This method returns 0 when the receiver is not in the NSRangeDateMode mode.

## See Also

### Accessing Object Values
- [var dateValue: Date](./datevalue.md)
  The date selected by the date picker.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdatepicker/timeinterval)*