# LiveCallerIDLookupManager

**Framework**: SMS and Call Reporting  
**Kind**: class

The entry point that provides access to a collection of functions that help manage the state of the Live Caller ID Lookup app extension.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
class LiveCallerIDLookupManager
```

## Mentions

- [Getting up-to-date calling and blocking information for your app](getting-up-to-date-calling-and-blocking-information-for-your-app.md)

#### Overview

You can use the provided functions to check whether your app extension is in an enabled state, open Settings to enable the extension, and manage refreshing your server data.

## Topics

### Checking status and fetching data
- [let extensionPointName: String](extensionpointname.md)
  The name of the extension point.
- [func openSettings() async throws](livecalleridlookupmanager/opensettings.md)
  Navigates to Settings so a person can configure the Live Caller ID Lookup app extension.
- [func refreshPIRParameters(forExtensionWithIdentifier: String) async throws](livecalleridlookupmanager/refreshpirparameters(forextensionwithidentifier:).md)
  Communicates with the system to refetch Private Information Retrieval (PIR) parameters from the server.
- [func reset(forExtensionWithIdentifier: String) async throws](livecalleridlookupmanager/reset(forextensionwithidentifier:).md)
  Resets the cache associated with the app extension.
- [func status(forExtensionWithIdentifier: String) -> CallLookupExtensionStatus](livecalleridlookupmanager/status(forextensionwithidentifier:).md)
  Queries the system to check the status of the app extension.
### Sharing the instance
- [static let shared: LiveCallerIDLookupManager](livecalleridlookupmanager/shared.md)
  The shared Live Caller ID Lookup manager instance for the app.
### Instance Methods
- [func refreshExtensionContext(forExtensionWithIdentifier: String) async throws](livecalleridlookupmanager/refreshextensioncontext(forextensionwithidentifier:).md)

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
- [struct LiveCallerIDLookupExtensionContext](livecalleridlookupextensioncontext.md)
  The information the system uses for configuration.
- [enum CallLookupExtensionStatus](calllookupextensionstatus.md)
  Returns a value with the current state of the app extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitylookup/livecalleridlookupmanager)*