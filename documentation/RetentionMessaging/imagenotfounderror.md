# ImageNotFoundError

**Framework**: Retention Messaging API  
**Kind**: dictionary

An error that indicates the system can’t find the image identifier.

**Availability**:
- Retention Messaging API 1.0+

## Declaration

```swift
object ImageNotFoundError
```

#### Overview

The [`Delete Image`](delete-image.md) endpoint returns this error if the [`imageIdentifier`](imageidentifier.md) doesn’t exist.

## See Also

- [object AltTextTooLongError](alttexttoolongerror.md)
  An error that indicates the alternative text for an image is too long.
- [object BodyTooLongError](bodytoolongerror.md)
  An error that indicates the body text is too long.
- [object ExistingPerformanceTestRunError](existingperformancetestrunerror.md)
  An error that indicates an error with an existing test.
- [object HeaderTooLongError](headertoolongerror.md)
  An error that indicates the header text is too long.
- [object ImageAlreadyExistsError](imagealreadyexistserror.md)
  An error that indicates the image identifier already exists.
- [object ImageInUseError](imageinuseerror.md)
  An error that indicates the image is currently in use as part of a message, so you can’t delete it.
- [object ImageNotApprovedError](imagenotapprovederror.md)
  An error that indicates the image isn’t in the approved state, so you can’t configure it as part of a default message.
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
- [object MaximumNumberOfImagesReachedError](maximumnumberofimagesreachederror.md)
  An error that indicates when you reach the maximum number of uploaded images.
- [object MaximumNumberOfMessagesReachedError](maximumnumberofmessagesreachederror.md)
  An error that indicates when you reach the maximum number of uploaded messages.
- [object MessageAlreadyExistsError](messagealreadyexistserror.md)
  An error that indicates the message identifier already exists.


---

*[View on Apple Developer](https://developer.apple.com/documentation/retentionmessaging/imagenotfounderror)*