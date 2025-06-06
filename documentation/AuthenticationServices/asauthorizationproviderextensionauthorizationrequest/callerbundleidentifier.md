# callerBundleIdentifier

**Framework**: Authentication Services  
**Kind**: property

The bundle ID of the app making the request.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
var callerBundleIdentifier: String { get }
```

## See Also

- [var callerTeamIdentifier: String](asauthorizationproviderextensionauthorizationrequest/callerteamidentifier.md)
  The team identifier of the app making the request.
- [var localizedCallerDisplayName: String](asauthorizationproviderextensionauthorizationrequest/localizedcallerdisplayname.md)
  The localized display name of the app making the request.
- [var isCallerManaged: Bool](asauthorizationproviderextensionauthorizationrequest/iscallermanaged.md)
  A Boolean value that indicates whether the app making the request is managed.
- [var extensionData: [AnyHashable : Any]](asauthorizationproviderextensionauthorizationrequest/extensiondata.md)
  Extension data from the Mobile Device Management (MDM) configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationproviderextensionauthorizationrequest/callerbundleidentifier)*