# NewSubmissionRequest

**Framework**: Notary API  
**Kind**: dictionary

Data that you provide when starting a submission to the notary service.

**Availability**:
- Notary API 2.0.0+

## Declaration

```swift
object NewSubmissionRequest
```

#### Discussion

Use a structure of this type as the HTTP body when you post to the [`Submit Software`](submit-software.md) endpoint.

## Topics

### Objects
- [object NewSubmissionRequest.Notifications](newsubmissionrequest/notifications-data.dictionary.md)
  A notification that the notary service sends you when notarization finishes.

## Properties

- `notifications` ([NewSubmissionRequest.Notifications]): An optional array of notifications that you want to receive when notarization finishes. Omit this key if you don’t need a notification.
- `sha256` (string) *(required)*: A cryptographic hash of the software that you want to notarize, computed using Secure Hashing Algorithm 2 (SHA-2) with a 256-bit digest. Supply the hash as a string of 64 hexadecimal digits. You must compute the hash from the exact version of the software that you plan to upload to Amazon S3.
- `submissionName` (string) *(required)*: The name of the file that you plan to submit. The service includes this name in its responses when you ask for the status of a submission, get a list of previous submissions, or get a log file corresponding to a submission. The file name doesn’t have to be unique among all your submissions, but making it so might help you to distinguish among submissions in service responses.

## See Also

- [Submit Software](submit-software.md)
  Start the process of uploading a new version of your software to the notary service.
- [object NewSubmissionResponse](newsubmissionresponse.md)
  The notary service’s response to a software submission.


---

*[View on Apple Developer](https://developer.apple.com/documentation/notaryapi/newsubmissionrequest)*