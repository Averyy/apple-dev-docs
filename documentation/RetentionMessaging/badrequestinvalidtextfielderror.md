# BadRequestInvalidTextFieldError

**Framework**: Retention Messaging API  
**Kind**: dictionary  
**Role**: Object

An error that indicates a text field in the request is invalid.

**Availability**:
- Retention Messaging API 1.5+

## Declaration

```
object BadRequestInvalidTextFieldError
```

## Mentions

- [Retention Messaging API changelog](./retention-messaging-changelog.md)

## Overview

This error occurs when a text field in the [`UploadMessageRequestBody`](./uploadmessagerequestbody.md) contains characters the system doesn’t allow, such as emoji. Each text field, including [`header`](./header.md), [`body`](./body.md), [`altText`](./alttext.md), and [`bulletPointText`](./bulletpointtext.md), needs to be a valid UTF-8-encoded string that contains only allowed Unicode characters. To resolve this error, remove any disallowed characters from the text fields and upload the message again.

## Properties

- `errorCode` (number): **Allowed Values**: `4000250`
- `errorMessage` (string): **Allowed Values**: `Invalid request. A text field is invalid.`

## See Also

### Errors for bad requests
- [object BadRequestAboveImageRequiresAnImageError](./badrequestaboveimagerequiresanimageerror.md)
  An error that indicates that no image object is included, but the request indicates that the header should be placed above the image.
- [object BadRequestAppTransactionIdForUnsupportedEndpointError](./badrequestapptransactionidforunsupportedendpointerror.md)
  An error that indicates the endpoint doesn’t support app transaction identifiers instead of transaction identifiers.
- [object BadRequestBulletPointTextTooLongError](./badrequestbulletpointtexttoolongerror.md)
  An error that indicates the text for a bullet point is too long.
- [object BadRequestImageSizeError](./badrequestimagesizeerror.md)
  An error that indicates the image size provided is invalid.
- [object BadRequestRealtimeUrlError](./badrequestrealtimeurlerror.md)
  An error that indicates the URL is invalid.
- [object BadRequestTooManyBulletPointsError](./badrequesttoomanybulletpointserror.md)
  An error that indicates there are too many bullet points.
- [object BadRequestTransactionIdError](./badrequesttransactioniderror.md)
  An error that indicates the transaction ID is invalid.
- [object BadRequestTransactionIdNotOtidError](./badrequesttransactionidnototiderror.md)
  An error that indicates the transaction ID provided is not an original transaction ID.
- [object BadRequestTransactionIdNotSupportedForFamilySharingError](./badrequesttransactionidnotsupportedforfamilysharingerror.md)
  An error that indicates that the endpoint doesn’t support transactions for products the customer receives through Family Sharing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/retentionmessaging/badrequestinvalidtextfielderror)*