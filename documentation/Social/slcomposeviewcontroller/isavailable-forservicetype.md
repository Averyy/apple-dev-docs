# isAvailable(forServiceType:)

**Framework**: Social  
**Kind**: method

Returns A Boolean value that indicates whether you can send a request for a particular service type.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
class func isAvailable(forServiceType serviceType: String!) -> Bool
```

#### Return Value

Returns a Boolean value that indicates whether the service is accessible and whether at least one account is set up.

#### Discussion

For the account to be available, the user must be logged into the social service in the device settings.

## Parameters

- `serviceType`: The social networking service. For a list of possible values, see Service Type Constants.

## See Also

- [var serviceType: String!](slcomposeviewcontroller/servicetype.md)
  Specifies the social-networking service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/social/slcomposeviewcontroller/isavailable(forservicetype:))*