# NewSubmissionResponse

**Framework**: Notary API  
**Kind**: dictionary

The notary service’s response to a software submission.

**Availability**:
- Notary API 2.0.0+

## Declaration

```swift
object NewSubmissionResponse
```

#### Discussion

You receive a structure of this type in response to a call to the [`Submit Software`](submit-software.md) endpoint. Use the temporary security credentials this response contains to make a call to Amazon S3 to upload your software.

## Topics

### Objects
- [object NewSubmissionResponse.Data](newsubmissionresponse/data-data.dictionary.md)
  Information that the notary service provides for uploading your software for notarization and tracking the submission.
- [object NewSubmissionResponse.Meta](newsubmissionresponse/meta-data.dictionary.md)
  An empty object.

## See Also

- [Submit Software](submit-software.md)
  Start the process of uploading a new version of your software to the notary service.
- [object NewSubmissionRequest](newsubmissionrequest.md)
  Data that you provide when starting a submission to the notary service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/notaryapi/newsubmissionresponse)*