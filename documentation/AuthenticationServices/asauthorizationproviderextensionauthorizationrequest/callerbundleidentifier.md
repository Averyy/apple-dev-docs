# callerBundleIdentifier

**Framework**: Authentication Services  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, copy, readonly) NSString * callerBundleIdentifier;
```

## See Also

### Getting Context
- [var callerTeamIdentifier: String](./callerteamidentifier.md)
  The team identifier of the app making the request.
- [var localizedCallerDisplayName: String](./localizedcallerdisplayname.md)
  The localized display name of the app making the request.
- [var isCallerManaged: Bool](./iscallermanaged.md)
  A Boolean value that indicates whether the app making the request is managed.
- [var extensionData: [AnyHashable : Any]](./extensiondata.md)
  Extension data from the Mobile Device Management (MDM) configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationproviderextensionauthorizationrequest/callerbundleidentifier)*