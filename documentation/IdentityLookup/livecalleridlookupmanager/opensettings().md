# openSettings()

**Framework**: SMS and Call Reporting  
**Kind**: method  
**Role**: Instance Method

Navigates to Settings so a person can configure the Live Caller ID Lookup app extension.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
func openSettings() async throws
```

## Mentions

- [Getting up-to-date calling and blocking information for your app](../getting-up-to-date-calling-and-blocking-information-for-your-app.md)

## See Also

### Checking status and fetching data
- [let extensionPointName: String](../extensionpointname.md)
  The name of the extension point.
- [func refreshPIRParameters(forExtensionWithIdentifier: String) async throws](./refreshpirparameters%28forextensionwithidentifier%29.md)
  Communicates with the system to refetch Private Information Retrieval (PIR) parameters from the server.
- [func reset(forExtensionWithIdentifier: String) async throws](./reset%28forextensionwithidentifier%29.md)
  Resets the cache associated with the app extension.
- [func status(forExtensionWithIdentifier: String) -> CallLookupExtensionStatus](./status%28forextensionwithidentifier%29.md)
  Queries the system to check the status of the app extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitylookup/livecalleridlookupmanager/opensettings())*