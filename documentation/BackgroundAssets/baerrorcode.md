# BAErrorCode

**Framework**: Background Assets  
**Kind**: enum  
**Role**: Enumeration

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 18.4+
- visionOS 2.4+

## Declaration

```swift
enum BAErrorCode
```

```c
enum BAErrorCode : NSInteger;
```

## Topics

### Error codes
- [BAErrorCode.callFromExtensionNotAllowed](./baerrorcode/callfromextensionnotallowed.md)
- [BAErrorCode.callFromInactiveProcessNotAllowed](./baerrorcode/callfrominactiveprocessnotallowed.md)
- [BAErrorCode.callerConnectionInvalid](./baerrorcode/callerconnectioninvalid.md)
- [BAErrorCode.callerConnectionNotAccepted](./baerrorcode/callerconnectionnotaccepted.md)
- [BAErrorCode.downloadAlreadyFailed](./baerrorcode/downloadalreadyfailed.md)
- [BAErrorCode.downloadAlreadyScheduled](./baerrorcode/downloadalreadyscheduled.md)
- [BAErrorCode.downloadBackgroundActivityProhibited](./baerrorcode/downloadbackgroundactivityprohibited.md)
- [BAErrorCode.downloadEssentialDownloadNotPermitted](./baerrorcode/downloadessentialdownloadnotpermitted.md)
- [BAErrorCode.downloadFailedToStart](./baerrorcode/downloadfailedtostart.md)
- [BAErrorCode.downloadInvalid](./baerrorcode/downloadinvalid.md)
- [BAErrorCode.downloadNotScheduled](./baerrorcode/downloadnotscheduled.md)
- [BAErrorCode.downloadWouldExceedAllowance](./baerrorcode/downloadwouldexceedallowance.md)
- [BAErrorCode.sessionDownloadAllowanceExceeded](./baerrorcode/sessiondownloadallowanceexceeded.md)
- [BAErrorCode.sessionDownloadDisallowedByAllowance](./baerrorcode/sessiondownloaddisallowedbyallowance.md)
- [BAErrorCode.sessionDownloadDisallowedByDomain](./baerrorcode/sessiondownloaddisallowedbydomain.md)
- [BAErrorCode.sessionDownloadNotPermittedBeforeAppLaunch](./baerrorcode/sessiondownloadnotpermittedbeforeapplaunch.md)
### Initializers
- [init?(rawValue: Int)](./baerrorcode/init%28rawvalue%29.md)
### Enumeration Cases
- [BAErrorCode.downloadDoesNotExist](./baerrorcode/downloaddoesnotexist.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Errors
- [enum ManagedBackgroundAssetsError](./managedbackgroundassetserror.md)
  An error for a managed asset pack.
- [let BAErrorDomain: String](./baerrordomain.md)
- [AssetPackManager.LocalAvailabilityError](./assetpackmanager/localavailabilityerror.md)
  An error that provides information about local asset pack availability, distinguishing between successes and failures.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/baerrorcode)*