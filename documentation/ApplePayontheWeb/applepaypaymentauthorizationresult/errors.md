# errors

**Framework**: Apple Pay on the Web  
**Kind**: property

A list of custom errors to display on the payment sheet.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```swift
sequence <ApplePayError> errors;
```

#### Discussion

List the errors on the payment sheet for the user to remedy. If there are multiple errors, list the most critical error first. For information about errors, see [`ApplePayError`](applepayerror.md).

## See Also

- [status](applepaypaymentauthorizationresult/status.md)
  The status code for the authorization result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/applepaypaymentauthorizationresult/errors)*