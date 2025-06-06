# kGSSICAppleSourceAppAuditToken

**Framework**: GSS  
**Kind**: var

The audit token of the app’s process.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.0+
- macOS 10.14+
- visionOS 1.0+

## Declaration

```swift
var kGSSICAppleSourceAppAuditToken: String { get }
```

#### Discussion

The value is an `audit_token_t` value wrapped in a `CFDataRef`.

## See Also

- [var kGSSICAppleSourceAppPID: String](kgssicapplesourceapppid.md)
  A number that indicates the process ID of the app.
- [var kGSSICAppleSourceAppSigningIdentity: String](kgssicapplesourceappsigningidentity.md)
  The bundle signing identity of the app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gss/kgssicapplesourceappaudittoken)*