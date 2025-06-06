# Create an App Store version submission

**Framework**: App Store Connect API  
**Kind**: httpRequest

Submit an App Store version to App Review.

**Availability**:
- App Store Connect API 1.2+

## Mentions

- [App Store Connect API 1.7 release notes](app-store-connect-api-1-7-release-notes.md)

#### Discussion

Use this endpoint to submit a version to the App Store. If the version is missing required information, this request fails and the response contains error messages that indicate the problems.

If the version’s `releaseType` attribute is `AFTER_APPROVAL`, after App Review approves the version App Store Connect  automatically releases it to the App Store.

##### Submit a Version to the App Store

## Request Body

The request body.

## See Also

- [Delete an App Store Version Submission](delete-v1-appstoreversionsubmissions-_id_.md)
  Remove a version from App Store review.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/post-v1-appstoreversionsubmissions)*