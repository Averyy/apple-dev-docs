# realUserStatus

**Framework**: Authentication Services  
**Kind**: property

A value that indicates whether the user appears to be a real person.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var realUserStatus: ASUserDetectionStatus { get }
```

#### Discussion

Use this property’s value as one piece of data when trying to prevent fraud. A value of [`ASUserDetectionStatus.likelyReal`](asuserdetectionstatus/likelyreal.md) is a hint that the system has a reasonably high confidence that the user is a real person, as opposed to an automated agent, but this isn’t a guarantee.

## See Also

- [enum ASUserDetectionStatus](asuserdetectionstatus.md)
  Possible values for the real user indicator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationappleidcredential/realuserstatus)*