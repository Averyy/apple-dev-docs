# alwaysAuthorizationDenied

**Framework**: Core Location  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates someone has not granted the always authorization to your app.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```objc
@property (nonatomic, readonly) BOOL alwaysAuthorizationDenied;
```

#### Discussion

This property is `true` in the `CLServiceSessionDiagnostic` of a [`CLServiceSession`](../clservicesession-pt7n.md) created with an [`CLServiceSession.AuthorizationRequirement.always`](../clservicesession-pt7n/authorizationrequirement/always.md)  goal if someone denies the app that authorization; otherwise `false`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clservicesessiondiagnostic/alwaysauthorizationdenied)*