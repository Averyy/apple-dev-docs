# businessInformation(for:)

**Framework**: TelephonyMessagingKit  
**Kind**: method

Requests business information for a specified handle.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+

## Declaration

```swift
final func businessInformation(for request: RCSService.BusinessInformationRequest) async throws -> RCSService.Business?
```

#### Return Value

The actual render information structure or error.

## Parameters

- `request`:   containing the request parameters.

## See Also

- [RCSService.BusinessInformationRequest](rcsservice/businessinformationrequest.md)
  A structure representing a request to retrieve information about a business.
- [RCSService.Business](rcsservice/business.md)
  Structure containing details about a business.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/businessinformation(for:))*