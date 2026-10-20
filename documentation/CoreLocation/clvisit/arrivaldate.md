# arrivalDate

**Framework**: Core Location  
**Kind**: property  
**Role**: Instance Property

The approximate time at which the user arrived at the specified location.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.15+

## Declaration

```swift
var arrivalDate: Date { get }
```

```objc
@property (nonatomic, copy, readonly) NSDate * arrivalDate;
```

#### Discussion

When the visit object does not include arrival information, this property is set to the date returned by the [`distantPast`](../../Foundation/nsdate/distantpast.md) method of [`NSDate`](../../Foundation/nsdate.md).

## See Also

### Getting the visit duration
- [var departureDate: Date](./departuredate.md)
  The approximate time at which the user left the specified location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clvisit/arrivaldate)*