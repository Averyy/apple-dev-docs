# UIApplicationExitsOnSuspend

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

A Boolean value indicating whether the app terminates, rather than moves to the background, when the app quits.

**Availability**:
- iOS 4.0+ - Deprecated in 13.0
- iPadOS 4.0+ - Deprecated in 13.0
- tvOS 9.0+ - Deprecated in 13.0
- visionOS 1.0+
- watchOS 2.0+ - Deprecated in 6.0

> **Deprecated**: The system now automatically suspends apps leaving the foreground when they don’t require background execution. For more information, see [About the background execution sequence](../../UIKit/about-the-background-execution-sequence.md).

## Details

- **Name**: `UIApplicationExitsOnSuspend` (Application does not run in background)
- **Type**: boolean

## See Also

### Termination
- [LSGetAppDiedEvents](./lsgetappdiedevents.md)
  A Boolean value indicating whether the app is notified when a child process dies.
- [NSSupportsSuddenTermination](./nssupportssuddentermination.md)
  A Boolean value indicating whether the system may terminate the app to log out or shut down more quickly.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/uiapplicationexitsonsuspend)*