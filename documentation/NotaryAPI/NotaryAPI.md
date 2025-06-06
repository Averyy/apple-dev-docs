# Notary API

**Framework**: Notary API  
**Kind**: module

Submit your macOS software for notarization through a web interface.

**Availability**:
- Notary API 2.0.0+

#### Overview

Notarization gives people confidence that your Developer ID-signed macOS software has been checked by Apple for malicious code. In addition to interacting with the notary service through Xcode or the `notarytool` command-line utility, you can bypass `notarytool` and interact directly with the service through its REST API. The Notary API is helpful for instances where you need to avoid a macOS dependency when uploading your app to the notary service, and provides endpoints that enable you to:

- Prepare the notary service to receive a new version of your software, and get credentials that you use to upload your software to an Amazon S3 endpoint.
- Check the status of a submission.
- Retrieve a log file that provides details about a submission.
- Get a list of your team’s previous submissions.

To learn how notarization works, see [`Notarizing macOS software before distribution`](https://developer.apple.com/documentation/Security/notarizing-macos-software-before-distribution). For details about using the notary service REST API to upload your software, see [`Submitting software for notarization over the web`](submitting-software-for-notarization-over-the-web.md).

## Topics

### Essentials
- [Submitting software for notarization over the web](submitting-software-for-notarization-over-the-web.md)
  Eliminate a dependency on macOS in your notarization workflow by interfacing directly with the notary service.
### Software submission
- [Submit Software](submit-software.md)
  Start the process of uploading a new version of your software to the notary service.
- [object NewSubmissionRequest](newsubmissionrequest.md)
  Data that you provide when starting a submission to the notary service.
- [object NewSubmissionResponse](newsubmissionresponse.md)
  The notary service’s response to a software submission.
### Notarization results
- [Get Submission Status](get-submission-status.md)
  Fetch the status of a software notarization submission.
- [object SubmissionResponse](submissionresponse.md)
  The notary service’s response to a request for the status of a submission.
- [Get Submission Log](get-submission-log.md)
  Fetch details about a single completed notarization.
- [object SubmissionLogURLResponse](submissionlogurlresponse.md)
  The notary service’s response to a request for the log information about a completed submission.
### History
- [Get Previous Submissions](get-previous-submissions.md)
  Fetch a list of your team’s previous notarization submissions.
- [object SubmissionListResponse](submissionlistresponse.md)
  The notary service’s response to a request for information about your team’s previous submissions.
### Errors
- [object ErrorResponse](errorresponse.md)
  The notary service’s response when an error occurs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/NotaryAPI)*