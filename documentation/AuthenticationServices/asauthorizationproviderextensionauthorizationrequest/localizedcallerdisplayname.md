# localizedCallerDisplayName

**Framework**: Authentication Services  
**Kind**: property  
**Role**: Instance Property

The localized display name of the app making the request.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var localizedCallerDisplayName: String { get }
```

```objc
@property (nonatomic, readonly) NSString * localizedCallerDisplayName;
```

## See Also

### Getting Context
- [var callerBundleIdentifier: String](./callerbundleidentifier.md)
  The bundle ID of the app making the request.
- [var callerTeamIdentifier: String](./callerteamidentifier.md)
  The team identifier of the app making the request.
- [var isCallerManaged: Bool](./iscallermanaged.md)
  A Boolean value that indicates whether the app making the request is managed.
- [var extensionData: [AnyHashable : Any]](./extensiondata.md)
  Extension data from the Mobile Device Management (MDM) configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationproviderextensionauthorizationrequest/localizedcallerdisplayname)*