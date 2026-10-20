# CiTestResult

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

The outcome of a single test case in an Xcode Cloud test action, including its pass/fail status and duration.

**Availability**:
- App Store Connect API 1.5+

## Declaration

```
object CiTestResult
```

## Topics

### Objects
- [object CiTestResult.Attributes](./citestresult/attributes-data.dictionary.md)
  The attributes that describe a Test Results resource.

## Properties

- `attributes` (CiTestResult.Attributes): The attributes that describe the Test Results resource.
- `id` (string) *(required)*: The opaque resource ID that uniquely identifies a Test Results resource.
- `links` (ResourceLinks): The navigational links that include the self-link.
- `type` (string) *(required)*: The resource type.

  **Allowed Values**: `ciTestResults`

## See Also

### Objects and types
- [object CiTestResultResponse](./citestresultresponse.md)
  The response body for endpoints that read a single test result from an Xcode Cloud build action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/citestresult)*