# extensionData

**Framework**: Authentication Services  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, readonly) NSDictionary * extensionData;
```

## See Also

### Getting Context
- [var callerBundleIdentifier: String](./callerbundleidentifier.md)
  The bundle ID of the app making the request.
- [var callerTeamIdentifier: String](./callerteamidentifier.md)
  The team identifier of the app making the request.
- [var localizedCallerDisplayName: String](./localizedcallerdisplayname.md)
  The localized display name of the app making the request.
- [var isCallerManaged: Bool](./iscallermanaged.md)
  A Boolean value that indicates whether the app making the request is managed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationproviderextensionauthorizationrequest/extensiondata)*