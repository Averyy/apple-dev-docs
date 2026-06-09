# AppsBetaTesterUsagesV1MetricResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

A response that contains one or more beta app tester metric resources.

**Availability**:
- App Store Connect API 3.1+

## Declaration

```swift
object AppsBetaTesterUsagesV1MetricResponse
```

## Topics

### Objects
- [object AppsBetaTesterUsagesV1MetricResponse.Data](appsbetatesterusagesv1metricresponse/data-data.dictionary.md)
  The request body you use to update an apps beta tester usages v1metric response.

## Properties

- `data` ([AppsBetaTesterUsagesV1MetricResponse.Data]) *(required)*
- `included` ([BetaTester])
- `links` (PagedDocumentLinks) *(required)*
- `meta` (PagingInformation)

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
- [object BetaTesterBuildsLinkagesRequest](betatesterbuildslinkagesrequest.md)
  A request body you use to add or remove builds from a beta tester.
- [object BetaTesterBuildsLinkagesResponse](betatesterbuildslinkagesresponse.md)
  A response body that contains a list of related resource IDs.
- [object BetaTesterCreateRequest](betatestercreaterequest.md)
  The request body you use to create a BetaTester.
- [object BetaTesterResponse](betatesterresponse.md)
  The response body for endpoints that create, read, or modify a TestFlight beta tester.
- [object BetaTestersResponse](betatestersresponse.md)
  The response body for endpoints that list TestFlight beta testers.
- [object BetaTesterUsagesV1MetricResponse](betatesterusagesv1metricresponse.md)
  A response that contains one or more beta tester usage metric resources.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/appsbetatesterusagesv1metricresponse)*