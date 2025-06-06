# callerTeamIdentifier

**Framework**: Authentication Services  
**Kind**: property

The team identifier of the app making the request.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var callerTeamIdentifier: String { get }
```

## See Also

- [var callerBundleIdentifier: String](asauthorizationproviderextensionauthorizationrequest/callerbundleidentifier.md)
  The bundle ID of the app making the request.
- [var localizedCallerDisplayName: String](asauthorizationproviderextensionauthorizationrequest/localizedcallerdisplayname.md)
  The localized display name of the app making the request.
- [var isCallerManaged: Bool](asauthorizationproviderextensionauthorizationrequest/iscallermanaged.md)
  A Boolean value that indicates whether the app making the request is managed.
- [var extensionData: [AnyHashable : Any]](asauthorizationproviderextensionauthorizationrequest/extensiondata.md)
  Extension data from the Mobile Device Management (MDM) configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationproviderextensionauthorizationrequest/callerteamidentifier)*