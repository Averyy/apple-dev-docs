# Error codes

**Framework**: Retention Messaging API

Understand the error codes that Retention Messaging API responses return.

## Topics

### Errors
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
- [object MaximumNumberOfImagesReachedError](maximumnumberofimagesreachederror.md)
  An error that indicates when you reach the maximum number of uploaded images.
- [object MaximumNumberOfMessagesReachedError](maximumnumberofmessagesreachederror.md)
  An error that indicates when you reach the maximum number of uploaded messages.
- [object MessageAlreadyExistsError](messagealreadyexistserror.md)
  An error that indicates the message identifier already exists.
- [object MessageNotApprovedError](messagenotapprovederror.md)
  An error that indicates the message isn’t in the approved state, so you can’t configure it as a default message.
- [object MessageNotFoundError](messagenotfounderror.md)
  An error that indicates the system can’t find the message identifier.
- [object PerformanceTestRunNotFoundError](performancetestrunnotfounderror.md)
  An error the API returns if the service can’t find the specified test run.
- [object RateLimitExceededError](ratelimitexceedederror.md)
  An error that indicates the request exceeded the rate limit.
- [object RealtimeUrlNotFoundError](realtimeurlnotfounderror.md)
  An error that indicates that the URL for your endpoint isn’t configured.
### Errors for bad requests
- [object BadRequestAboveImageRequiresAnImageError](badrequestaboveimagerequiresanimageerror.md)
  An error that indicates that no image object is included, but the request indicates that the header should be placed above the image.
- [object BadRequestAppTransactionIdForUnsupportedEndpointError](badrequestapptransactionidforunsupportedendpointerror.md)
  An error that indicates the endpoint doesn’t support app transaction identifiers instead of transaction identifiers.
- [object BadRequestBulletPointTextTooLongError](badrequestbulletpointtexttoolongerror.md)
  An error that indicates the text for a bullet point is too long.
- [object BadRequestImageSizeError](badrequestimagesizeerror.md)
  An error that indicates the image size provided is invalid.
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
### Errors to retry
- [object GeneralInternalError](generalinternalerror.md)
  An error that indicates a general internal error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/retentionmessaging/error-codes)*