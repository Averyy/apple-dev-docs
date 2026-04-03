# MessageAlreadyExistsError

**Framework**: Retention Messaging API  
**Kind**: dictionary

An error that indicates the message identifier already exists.

**Availability**:
- Retention Messaging API 1.0+

## Declaration

```swift
object MessageAlreadyExistsError
```

#### Overview

The [`Upload Message`](upload-message.md) endpoint returns this error when the [`messageIdentifier`](messageidentifier.md) already exists.

## Properties

- `errorCode` (number)
- `errorMessage` (string)

## See Also

- [object AltTextTooLongError](alttexttoolongerror.md)
  An error that indicates the alternative text for an image is too long.
- [object BodyTooLongError](bodytoolongerror.md)
  An error that indicates the body text is too long.
- [object DefaultMessageNotFoundError](defaultmessagenotfounderror.md)
  An error that indicates a default message isn’t configured.
- [object ExistingPerformanceTestRunError](existingperformancetestrunerror.md)
  An error that indicates an error with an existing test.
- [object ForbiddenNoPassingTestError](forbiddennopassingtesterror.md)
  An error that indicates that passing a performance test is required before you can set a URL for the production environment.
- [object HeaderTooLongError](headertoolongerror.md)
  An error that indicates the header text is too long.
- [object ImageAlreadyExistsError](imagealreadyexistserror.md)
  An error that indicates the image identifier already exists.
- [object ImageInUseError](imageinuseerror.md)
  An error that indicates the image is currently in use as part of a message, so you can’t delete it.
- [object ImageNotApprovedError](imagenotapprovederror.md)
  An error that indicates the image isn’t in the approved state, so you can’t configure it as part of a default message.
- [object ImageNotFoundError](imagenotfounderror.md)
  An error that indicates the system can’t find the image identifier.
- [object InvalidImageError](invalidimageerror.md)
  An error that indicates the image that’s uploading is invalid.
- [object InvalidLocaleError](invalidlocaleerror.md)
  An error that indicates the locale is invalid.
- [object InvalidPerformanceTestRequestError](invalidperformancetestrequesterror.md)
  An error the API returns that indicates the performance test request is invalid.
- [object InvalidProductIdError](invalidproductiderror.md)
  An error that indicates the product ID is invalid.
- [object InvalidRequestIdError](invalidrequestiderror.md)
  An error that indicates the request ID is invalid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/retentionmessaging/messagealreadyexistserror)*