# init(forServiceType:requestMethod:url:parameters:)

**Framework**: Social  
**Kind**: init

Initializes a newly created request object with the specified properties.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+

## Declaration

```swift
init!(forServiceType serviceType: String!, requestMethod: SLRequestMethod, url: URL!, parameters: [AnyHashable : Any]!)
```

#### Return Value

The newly initialized request object.

#### Discussion

Use this method to initialize an `SLRequest`. The value and formatting of each parameter is dependent on the target service.

## Parameters

- `serviceType`: The social networking service type. For possible values, see  .
- `requestMethod`: The method to use for this HTTP request. For possible values, see  .
- `url`: The destination URL for this HTTP request. The values and formatting for the URL are dependent on the target service and are documented by the service provider. For links to documentation for the supported services, see Table 1 in  .
- `parameters`: The parameters for this HTTP request. The values and formatting are dependent on the target service and are documented by the service provider. For links to documentation for the supported services, see Table 1 in  .

## See Also

- [let SLServiceTypeFacebook: String](slservicetypefacebook.md)
- [let SLServiceTypeTwitter: String](slservicetypetwitter.md)
- [let SLServiceTypeSinaWeibo: String](slservicetypesinaweibo.md)
- [let SLServiceTypeLinkedIn: String](slservicetypelinkedin.md)
- [let SLServiceTypeTencentWeibo: String](slservicetypetencentweibo.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/social/slrequest/init(forservicetype:requestmethod:url:parameters:))*