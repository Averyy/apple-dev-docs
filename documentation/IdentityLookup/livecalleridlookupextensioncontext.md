# LiveCallerIDLookupExtensionContext

**Framework**: SMS and Call Reporting  
**Kind**: struct

The information the system uses for configuration.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
struct LiveCallerIDLookupExtensionContext
```

## Mentions

- [Getting up-to-date calling and blocking information for your app](getting-up-to-date-calling-and-blocking-information-for-your-app.md)

#### Overview

The extension context allows the system to obtain information from your app.

## Topics

### Initializing the app extension context
- [init(serviceURL: URL, tokenIssuerURL: URL, userTierToken: Data)](livecalleridlookupextensioncontext/init(serviceurl:tokenissuerurl:usertiertoken:).md)
  Creates the app extension context.
### Configuring the system
- [let serviceURL: URL](livecalleridlookupextensioncontext/serviceurl.md)
  The endpoint of the service to fetch identity and blocking information.
- [let tokenIssuerURL: URL](livecalleridlookupextensioncontext/tokenissuerurl.md)
  The URL of the Privacy Pass token issuer.
- [let userTierToken: Data](livecalleridlookupextensioncontext/usertiertoken.md)
  An HTTP bearer token that authenticates the person using your app.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Understanding how Live Caller ID Lookup preserves privacy](understanding-how-live-caller-id-lookup-preserves-privacy.md)
  Use Live Caller ID Lookup to protect user privacy by hiding the client’s IP address, using anonymous authentication, and hiding the incoming phone number.
- [Formatting data for blocking and identity information](formatting-data-for-blocking-and-identity-information.md)
  Set up your PIR payload for call blocking and identity information.
- [Setting up the HTTP endpoints for Live Caller ID Lookup](setting-up-the-http-endpoints-for-live-caller-id-lookup.md)
  Connect the on-device system to your server.
- [Getting up-to-date calling and blocking information for your app](getting-up-to-date-calling-and-blocking-information-for-your-app.md)
  Implement the Live Caller ID Lookup app extension to provide call-blocking and identity services.
- [protocol LiveCallerIDLookupProtocol](livecalleridlookupprotocol.md)
  Information the system uses to query the app extension for context.
- [protocol LiveCallerIDLookupExtensionConfiguration](livecalleridlookupextensionconfiguration.md)
  An object that allows the system to query the app extension.
- [enum CallLookupExtensionStatus](calllookupextensionstatus.md)
  Returns a value with the current state of the app extension.
- [class LiveCallerIDLookupManager](livecalleridlookupmanager.md)
  The entry point that provides access to a collection of functions that help manage the state of the Live Caller ID Lookup app extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitylookup/livecalleridlookupextensioncontext)*