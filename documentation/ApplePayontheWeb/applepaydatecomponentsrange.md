# ApplePayDateComponentsRange

**Framework**: Apple Pay on the Web  
**Kind**: struct

A dictionary that specifies the start and end dates for a range of time.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```swift
dictionary ApplePayDateComponentsRange {
	required ApplePayDateComponents startDateComponents;
	required ApplePayDateComponents endDateComponents;
};
```

## Topics

### Start and End Dates of the Range
- [startDateComponents](applepaydatecomponentsrange/startdatecomponents.md)
  The start date and time of the range.
- [endDateComponents](applepaydatecomponentsrange/enddatecomponents.md)
  The end date and time of the range.
- [ApplePayDateComponents](applepaydatecomponents.md)
  A dictionary that specifies the values for the calendrical units for a date.

## See Also

- [label](applepayshippingmethod/label.md)
  A short description of the shipping method.
- [detail](applepayshippingmethod/detail.md)
  Additional description of the shipping method.
- [dateComponentsRange](applepayshippingmethod/datecomponentsrange.md)
  The expected range of dates for shipping or picking up an item.
- [identifier](applepayshippingmethod/identifier.md)
  A client-defined value used to identify this shipping method.
- [amount](applepayshippingmethod/amount.md)
  The nonnegative cost associated with this shipping method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/applepaydatecomponentsrange)*