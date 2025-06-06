# refreshPIRParameters(forExtensionWithIdentifier:)

**Framework**: SMS and Call Reporting  
**Kind**: method

Communicates with the system to refetch Private Information Retrieval (PIR) parameters from the server.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
func refreshPIRParameters(forExtensionWithIdentifier identifier: String) async throws
```

## Mentions

- [Getting up-to-date calling and blocking information for your app](getting-up-to-date-calling-and-blocking-information-for-your-app.md)

#### Discussion

This throws an error when the system can’t referesh the PIR parameters.

## Parameters

- `identifier`: The identifier for the app extension.

## See Also

- [let extensionPointName: String](extensionpointname.md)
  The name of the extension point.
- [func openSettings() async throws](livecalleridlookupmanager/opensettings.md)
  Navigates to Settings so a person can configure the Live Caller ID Lookup app extension.
- [func reset(forExtensionWithIdentifier: String) async throws](livecalleridlookupmanager/reset(forextensionwithidentifier:).md)
  Resets the cache associated with the app extension.
- [func status(forExtensionWithIdentifier: String) -> CallLookupExtensionStatus](livecalleridlookupmanager/status(forextensionwithidentifier:).md)
  Queries the system to check the status of the app extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitylookup/livecalleridlookupmanager/refreshpirparameters(forextensionwithidentifier:))*