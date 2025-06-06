# LiveCallerIDLookupProtocol

**Framework**: SMS and Call Reporting  
**Kind**: protocol

Information the system uses to query the app extension for context.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
protocol LiveCallerIDLookupProtocol : AppExtension
```

## Mentions

- [Getting up-to-date calling and blocking information for your app](getting-up-to-date-calling-and-blocking-information-for-your-app.md)

## Topics

### Setting extension context
- [var context: LiveCallerIDLookupExtensionContext](livecalleridlookupprotocol/context.md)
  Information you use to connect to your server.

## Relationships

### Inherits From
- [AppExtension](../ExtensionFoundation/AppExtension.md)

## See Also

- [Understanding how Live Caller ID Lookup preserves privacy](understanding-how-live-caller-id-lookup-preserves-privacy.md)
  Use Live Caller ID Lookup to protect user privacy by hiding the client’s IP address, using anonymous authentication, and hiding the incoming phone number.
- [Formatting data for blocking and identity information](formatting-data-for-blocking-and-identity-information.md)
  Set up your PIR payload for call blocking and identity information.
- [Setting up the HTTP endpoints for Live Caller ID Lookup](setting-up-the-http-endpoints-for-live-caller-id-lookup.md)
  Connect the on-device system to your server.
- [Getting up-to-date calling and blocking information for your app](getting-up-to-date-calling-and-blocking-information-for-your-app.md)
  Implement the Live Caller ID Lookup app extension to provide call-blocking and identity services.
- [protocol LiveCallerIDLookupExtensionConfiguration](livecalleridlookupextensionconfiguration.md)
  An object that allows the system to query the app extension.
- [struct LiveCallerIDLookupExtensionContext](livecalleridlookupextensioncontext.md)
  The information the system uses for configuration.
- [enum CallLookupExtensionStatus](calllookupextensionstatus.md)
  Returns a value with the current state of the app extension.
- [class LiveCallerIDLookupManager](livecalleridlookupmanager.md)
  The entry point that provides access to a collection of functions that help manage the state of the Live Caller ID Lookup app extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitylookup/livecalleridlookupprotocol)*