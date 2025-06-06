# openSettings()

**Framework**: SMS and Call Reporting  
**Kind**: method

Navigates to Settings so a person can configure the Live Caller ID Lookup app extension.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
func openSettings() async throws
```

## Mentions

- [Getting up-to-date calling and blocking information for your app](getting-up-to-date-calling-and-blocking-information-for-your-app.md)

## See Also

- [let extensionPointName: String](extensionpointname.md)
  The name of the extension point.
- [func refreshPIRParameters(forExtensionWithIdentifier: String) async throws](livecalleridlookupmanager/refreshpirparameters(forextensionwithidentifier:).md)
  Communicates with the system to refetch Private Information Retrieval (PIR) parameters from the server.
- [func reset(forExtensionWithIdentifier: String) async throws](livecalleridlookupmanager/reset(forextensionwithidentifier:).md)
  Resets the cache associated with the app extension.
- [func status(forExtensionWithIdentifier: String) -> CallLookupExtensionStatus](livecalleridlookupmanager/status(forextensionwithidentifier:).md)
  Queries the system to check the status of the app extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitylookup/livecalleridlookupmanager/opensettings())*