# userTierToken

**Framework**: SMS and Call Reporting  
**Kind**: property

An HTTP bearer token that authenticates the person using your app.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
let userTierToken: Data
```

## Mentions

- [Getting up-to-date calling and blocking information for your app](getting-up-to-date-calling-and-blocking-information-for-your-app.md)

#### Discussion

The system sends this token to the Privacy Pass token issuer, which can verify whether it belongs to a valid user of your app. It then issues a Privacy Pass token.

## See Also

- [let serviceURL: URL](livecalleridlookupextensioncontext/serviceurl.md)
  The endpoint of the service to fetch identity and blocking information.
- [let tokenIssuerURL: URL](livecalleridlookupextensioncontext/tokenissuerurl.md)
  The URL of the Privacy Pass token issuer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitylookup/livecalleridlookupextensioncontext/usertiertoken)*