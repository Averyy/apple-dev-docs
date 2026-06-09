# BetaTesterBuildsLinkagesRequest

**Framework**: App Store Connect API  
**Kind**: dictionary

A request body you use to add or remove builds from a beta tester.

**Availability**:
- App Store Connect API 1.0+

## Declaration

```swift
object BetaTesterBuildsLinkagesRequest
```

## Topics

### Objects
- [object BetaTesterBuildsLinkagesRequest.Data](betatesterbuildslinkagesrequest/data-data.dictionary.md)
  The data element of the request body.

## Properties

- `data` ([BetaTesterBuildsLinkagesRequest.Data]) *(required)*: The types and IDs of related resources.

## See Also

- [object BetaTester](betatester.md)
  An individual enrolled as a beta tester in TestFlight, identified by their email address and associated with one or more apps or groups.
- [object BetaTestersWithoutIncludesResponse](betatesterswithoutincludesresponse.md)
  A response containing a list of TestFlight beta testers, without related resources.
- [object BetaTesterAppsLinkagesRequest](betatesterappslinkagesrequest.md)
  A request body you use to remove an app from a beta tester.
- [object BetaTesterAppsLinkagesResponse](betatesterappslinkagesresponse.md)
  A response body that contains a list of related resource IDs.
- [object BetaTesterBetaGroupsLinkagesRequest](betatesterbetagroupslinkagesrequest.md)
  A request body you use to add or remove beta groups from a beta tester.
- [object BetaTesterBetaGroupsLinkagesResponse](betatesterbetagroupslinkagesresponse.md)
  A response body that contains a list of related resource IDs.
- [object BetaTesterBuildsLinkagesResponse](betatesterbuildslinkagesresponse.md)
  A response body that contains a list of related resource IDs.
- [object BetaTesterCreateRequest](betatestercreaterequest.md)
  The request body you use to create a BetaTester.
- [object BetaTesterResponse](betatesterresponse.md)
  The response body for endpoints that create, read, or modify a TestFlight beta tester.
- [object BetaTestersResponse](betatestersresponse.md)
  The response body for endpoints that list TestFlight beta testers.
- [object AppsBetaTesterUsagesV1MetricResponse](appsbetatesterusagesv1metricresponse.md)
  A response that contains one or more beta app tester metric resources.
- [object BetaTesterUsagesV1MetricResponse](betatesterusagesv1metricresponse.md)
  A response that contains one or more beta tester usage metric resources.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/betatesterbuildslinkagesrequest)*