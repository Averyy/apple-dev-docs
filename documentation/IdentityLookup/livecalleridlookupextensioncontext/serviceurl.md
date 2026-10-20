# serviceURL

**Framework**: SMS and Call Reporting  
**Kind**: property  
**Role**: Instance Property

The endpoint of the service to fetch identity and blocking information.

**Availability**:
- iOS 18.0+ - Deprecated in 27.2
- iPadOS 18.0+ - Deprecated in 27.2
- Mac Catalyst 18.0+ - Deprecated in 27.2
- macOS 15.0+ - Deprecated in 27.2
- visionOS 2.0+ - Deprecated in 27.2

> **Deprecated**: Refer to Info.plist NSPIRConfiguration dictionary

## Declaration

```swift
let serviceURL: URL
```

## Mentions

- [Getting up-to-date calling and blocking information for your app](../getting-up-to-date-calling-and-blocking-information-for-your-app.md)
- [Setting up the HTTP endpoints for Live Caller ID Lookup](../setting-up-the-http-endpoints-for-live-caller-id-lookup.md)

## See Also

### Configuring the system
- [let tokenIssuerURL: URL](./tokenissuerurl.md)
  The URL of the Privacy Pass token issuer.
- [let userTierToken: Data](./usertiertoken.md)
  An HTTP bearer token that authenticates the person using your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitylookup/livecalleridlookupextensioncontext/serviceurl)*