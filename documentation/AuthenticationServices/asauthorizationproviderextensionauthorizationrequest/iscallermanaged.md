# isCallerManaged

**Framework**: Authentication Services  
**Kind**: property

A Boolean value that indicates whether the app making the request is managed.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var isCallerManaged: Bool { get }
```

## See Also

- [var callerBundleIdentifier: String](asauthorizationproviderextensionauthorizationrequest/callerbundleidentifier.md)
  The bundle ID of the app making the request.
- [var callerTeamIdentifier: String](asauthorizationproviderextensionauthorizationrequest/callerteamidentifier.md)
  The team identifier of the app making the request.
- [var localizedCallerDisplayName: String](asauthorizationproviderextensionauthorizationrequest/localizedcallerdisplayname.md)
  The localized display name of the app making the request.
- [var extensionData: [AnyHashable : Any]](asauthorizationproviderextensionauthorizationrequest/extensiondata.md)
  Extension data from the Mobile Device Management (MDM) configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationproviderextensionauthorizationrequest/iscallermanaged)*