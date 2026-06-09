# CiTestResultResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

The response body for endpoints that read a single test result from an Xcode Cloud build action.

**Availability**:
- App Store Connect API 1.5+

## Declaration

```swift
object CiTestResultResponse
```

## Properties

- `data` (CiTestResult) *(required)*: The resource data.
- `links` (DocumentLinks) *(required)*: The navigational links that include the self-link.

## See Also

- [object CiTestResult](citestresult.md)
  The outcome of a single test case in an Xcode Cloud test action, including its pass/fail status and duration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/citestresultresponse)*