# ASUserDetectionStatus

**Framework**: Authentication Services  
**Kind**: enum

Possible values for the real user indicator.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
enum ASUserDetectionStatus
```

## Topics

### User Status
- [ASUserDetectionStatus.likelyReal](asuserdetectionstatus/likelyreal.md)
  The user appears to be a real person.
- [ASUserDetectionStatus.unknown](asuserdetectionstatus/unknown.md)
  The system hasn’t determined whether the user might be a real person.
- [ASUserDetectionStatus.unsupported](asuserdetectionstatus/unsupported.md)
  The system can’t determine this user’s status as a real person.
### Initializers
- [init?(rawValue: Int)](asuserdetectionstatus/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var realUserStatus: ASUserDetectionStatus](asauthorizationappleidcredential/realuserstatus.md)
  A value that indicates whether the user appears to be a real person.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asuserdetectionstatus)*