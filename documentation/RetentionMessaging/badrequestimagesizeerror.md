# BadRequestImageSizeError

**Framework**: Retention Messaging API  
**Kind**: dictionary

An error that indicates the image size provided is invalid.

**Availability**:
- Retention Messaging API 1.4+

## Declaration

```swift
object BadRequestImageSizeError
```

## Properties

- `errorCode` (number)
- `errorMessage` (string)

## See Also

- [object BadRequestAboveImageRequiresAnImageError](badrequestaboveimagerequiresanimageerror.md)
  An error that indicates that no image object is included, but the request indicates that the header should be placed above the image.
- [object BadRequestAppTransactionIdForUnsupportedEndpointError](badrequestapptransactionidforunsupportedendpointerror.md)
  An error that indicates the endpoint doesn’t support app transaction identifiers instead of transaction identifiers.
- [object BadRequestBulletPointTextTooLongError](badrequestbulletpointtexttoolongerror.md)
  An error that indicates the text for a bullet point is too long.
- [object BadRequestRealtimeUrlError](badrequestrealtimeurlerror.md)
  An error that indicates the URL is invalid.
- [object BadRequestTooManyBulletPointsError](badrequesttoomanybulletpointserror.md)
  An error that indicates there are too many bullet points.
- [object BadRequestTransactionIdError](badrequesttransactioniderror.md)
  An error that indicates the transaction ID is invalid.
- [object BadRequestTransactionIdNotOtidError](badrequesttransactionidnototiderror.md)
  An error that indicates the transaction ID provided is not an original transaction ID.
- [object BadRequestTransactionIdNotSupportedForFamilySharingError](badrequesttransactionidnotsupportedforfamilysharingerror.md)
  An error that indicates that the endpoint doesn’t support transactions for products the customer receives through Family Sharing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/retentionmessaging/badrequestimagesizeerror)*