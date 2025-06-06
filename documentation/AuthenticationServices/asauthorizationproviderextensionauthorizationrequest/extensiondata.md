# extensionData

**Framework**: Authentication Services  
**Kind**: property

Extension data from the Mobile Device Management (MDM) configuration.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
var extensionData: [AnyHashable : Any] { get }
```

## See Also

- [var callerBundleIdentifier: String](asauthorizationproviderextensionauthorizationrequest/callerbundleidentifier.md)
  The bundle ID of the app making the request.
- [var callerTeamIdentifier: String](asauthorizationproviderextensionauthorizationrequest/callerteamidentifier.md)
  The team identifier of the app making the request.
- [var localizedCallerDisplayName: String](asauthorizationproviderextensionauthorizationrequest/localizedcallerdisplayname.md)
  The localized display name of the app making the request.
- [var isCallerManaged: Bool](asauthorizationproviderextensionauthorizationrequest/iscallermanaged.md)
  A Boolean value that indicates whether the app making the request is managed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationproviderextensionauthorizationrequest/extensiondata)*