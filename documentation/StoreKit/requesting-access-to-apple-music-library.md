# Requesting Access to Apple Music Library

**Framework**: StoreKit

Prompt the customer to authorize access to Apple Music library.

#### Overview

Your app must obtain permission from the customer before accessing Apple Music Library.

##### Provide a Purpose String in Infoplist

Provide a purpose string or usage description that describes how your app intends to use the user’s iCloud Music library or Apple Music catalog. Add the [`NSAppleMusicUsageDescription`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSAppleMusicUsageDescription) key to your app’s Info.plist. Set its value to a string that explains why your app needs access to Apple Music library. The system displays the string to the user when prompting them for authorization.

![Privacy - Media Library Usage Description](https://docs-assets.developer.apple.com/published/172797b315ff7d28ae7b00cf609dd514/media-3580813%402x.png)

> ❗ **Important**:  This key is required for apps that access the user’s music library. Apps crash when the key is absent.

 This key is required for apps that access the user’s music library. Apps crash when the key is absent.

See [`Requesting access to protected resources`](https://developer.apple.com/documentation/UIKit/requesting-access-to-protected-resources) for more details.

##### Request Authorization

The user determines whether apps can play items from the Apple Music catalog or add tracks to their iCloud Music library. They can grant or deny access when your app requests authorization. Because the user can change your app’s authorization status in Settings > Privacy > Media and Apple Music, be sure to call [`SKCloudServiceController`](skcloudservicecontroller.md)’s [`authorizationStatus()`](skcloudservicecontroller/authorizationstatus().md) before attempting to access their Apple Music library.

If the authorization status i`s` [`SKCloudServiceAuthorizationStatus.notDetermined`](skcloudserviceauthorizationstatus/notdetermined.md), call [`SKCloudServiceController`](skcloudservicecontroller.md)’s [`requestAuthorization(_:)`](skcloudservicecontroller/requestauthorization(_:).md) to prompt the user for access.

The system remembers the user’s answer so that subsequent calls to [`requestAuthorization(_:)`](skcloudservicecontroller/requestauthorization(_:).md) don’t prompt them again.

## See Also

- [class func authorizationStatus() -> SKCloudServiceAuthorizationStatus](skcloudservicecontroller/authorizationstatus.md)
  Returns the type of authorization the customer has for accessing the Music library on the device.
- [class func requestAuthorization((SKCloudServiceAuthorizationStatus) -> Void)](skcloudservicecontroller/requestauthorization(_:).md)
  Asks the customer for permission to access the Music library on the device.
- [enum SKCloudServiceAuthorizationStatus](skcloudserviceauthorizationstatus.md)
  Constants that indicate the type of authorization the customer has for accessing the Music library.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/requesting-access-to-apple-music-library)*