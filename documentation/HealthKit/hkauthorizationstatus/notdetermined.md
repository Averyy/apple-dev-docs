# HKAuthorizationStatus.notDetermined

**Framework**: HealthKit  
**Kind**: case

The user has not yet chosen to authorize access to the specified data type.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
case notDetermined
```

#### Discussion

Make sure your app requests proper authorization before calling any other HealthKit methods. For more information on setting up HealthKit, see `HealthKit`.

## See Also

- [HKAuthorizationStatus.sharingDenied](hkauthorizationstatus/sharingdenied.md)
  The user has explicitly denied your app permission to save data of the specified type.
- [HKAuthorizationStatus.sharingAuthorized](hkauthorizationstatus/sharingauthorized.md)
  The user has explicitly authorized your app to save data of the specified type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkauthorizationstatus/notdetermined)*