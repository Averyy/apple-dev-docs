# extensionPointName

**Framework**: SMS and Call Reporting  
**Kind**: var  
**Role**: Global Variable

The name of the extension point.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
let extensionPointName: String
```

## See Also

### Checking status and fetching data
- [func openSettings() async throws](./livecalleridlookupmanager/opensettings%28%29.md)
  Navigates to Settings so a person can configure the Live Caller ID Lookup app extension.
- [func refreshPIRParameters(forExtensionWithIdentifier: String) async throws](./livecalleridlookupmanager/refreshpirparameters%28forextensionwithidentifier%29.md)
  Communicates with the system to refetch Private Information Retrieval (PIR) parameters from the server.
- [func reset(forExtensionWithIdentifier: String) async throws](./livecalleridlookupmanager/reset%28forextensionwithidentifier%29.md)
  Resets the cache associated with the app extension.
- [func status(forExtensionWithIdentifier: String) -> CallLookupExtensionStatus](./livecalleridlookupmanager/status%28forextensionwithidentifier%29.md)
  Queries the system to check the status of the app extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitylookup/extensionpointname)*