# CLServiceSession.AuthorizationRequirement

**Framework**: Core Location  
**Kind**: enum  
**Role**: Enumeration

Values that describe when the service session needs to request authorization.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- tvOS 18.0+
- visionOS 1.0+
- watchOS 11.0+

## Declaration

```swift
enum AuthorizationRequirement
```

## Topics

### Authorization requirement values
- [CLServiceSession.AuthorizationRequirement.always](./authorizationrequirement/always.md)
- [CLServiceSession.AuthorizationRequirement.none](./authorizationrequirement/none.md)
- [CLServiceSession.AuthorizationRequirement.whenInUse](./authorizationrequirement/wheninuse.md)

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)

## See Also

### Creating a session
- [init(authorization: CLServiceSession.AuthorizationRequirement)](./init%28authorization%29.md)
  Creates a services session by using the authorization mode you specify.
- [init(authorization: CLServiceSession.AuthorizationRequirement, fullAccuracyPurposeKey: String)](./init%28authorization,fullaccuracypurposekey%29.md)
  Creates a services session by using the authorization mode and purpose key you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clservicesession-pt7n/authorizationrequirement)*