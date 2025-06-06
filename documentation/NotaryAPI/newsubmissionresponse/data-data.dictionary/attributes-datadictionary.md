# NewSubmissionResponse.Data.Attributes

**Framework**: Notary API  
**Kind**: dictionary

Information that you use to upload your software for notarization.

**Availability**:
- Notary API 2.0.0+

## Declaration

```swift
object NewSubmissionResponse.Data.Attributes
```

#### Discussion

Use the temporary security credentials in this object, along with the bucket and object, to upload your software to Amazon S3. A good way to do this is with the `boto3` library provided by Amazon, as described in [`Submitting software for notarization over the web`](submitting-software-for-notarization-over-the-web.md). Be sure to use the S3 credentials before they expire, which happens 12 hours after you receive them.

For more information about using this library and accessing Amazon S3, see the documentation on [`https://aws.amazon.com`](https://developer.apple.comhttps://aws.amazon.com).


---

*[View on Apple Developer](https://developer.apple.com/documentation/notaryapi/newsubmissionresponse/data-data.dictionary/attributes-data.dictionary)*