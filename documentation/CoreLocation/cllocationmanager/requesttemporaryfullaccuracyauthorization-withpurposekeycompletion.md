# requestTemporaryFullAccuracyAuthorization(withPurposeKey:completion:)

**Framework**: Core Location  
**Kind**: method

Requests permission to temporarily use location services with full accuracy and reports the results to the provided completion handler.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
func requestTemporaryFullAccuracyAuthorization(withPurposeKey purposeKey: String) async throws
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func requestTemporaryFullAccuracyAuthorization(withPurposeKey purposeKey: String) async throws
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

After the user gives permission for your app to use location data with full accuracy, your app can access that data in the foreground or in the background, until its permission automatically expires. Expiration is postponed while your app is actively in use. For example, expiration is postponed while your app in the foreground, and while a Continuous Background Location session is active with the background location indicator enabled. This approach to expiration allows apps to provide experiences that require full accuracy, such as fitness and navigation apps, even if the user doesn’t grant persistent access for full accuracy.

The completion closure is guaranteed to be called after the request is completed, which includes the user granting access, the user declining, or an error that prevented displaying the prompt. The closure is always called in the same threading context as [`CLLocationManagerDelegate`](cllocationmanagerdelegate.md) methods. If the prompt was successfully displayed to the user, the callback’s `error` parameter is `nil`.

The request always fails with a [`CLError.Code.promptDeclined`](clerror-swift.struct/code/promptdeclined.md) error in the following cases:

- The `Info.plist` file doesn’t have an entry for the given `purposeKey` value.
- The app is already authorized for full accuracy.
- The app is in the background.

If the closure is called with an error, log the error for debugging purposes, and retry the request again the next time the user performs the action that caused you to request precise location information.

## Parameters

- `purposeKey`: A key in the   dictionary of the app’s   file.  The value for this key is an app-provided string that describes the reason for accessing location data with full accuracy.  To localize a usage description, add an entry to your   file with the same key you provide for this parameter.
- `completion`: A closure to execute after authorization status changes. This closure takes a single   parameter, which is   if the prompt was displayed to the user, or an error object describing why the prompt couldn’t be displayed.

## See Also

- [func requestWhenInUseAuthorization()](cllocationmanager/requestwheninuseauthorization.md)
  Requests the user’s permission to use location services while the app is in use.
- [func requestAlwaysAuthorization()](cllocationmanager/requestalwaysauthorization.md)
  Requests the user’s permission to use location services regardless of whether the app is in use.
- [func requestTemporaryFullAccuracyAuthorization(withPurposeKey: String)](cllocationmanager/requesttemporaryfullaccuracyauthorization(withpurposekey:).md)
  Requests permission to temporarily use location services with full accuracy.
- [var authorizationStatus: CLAuthorizationStatus](cllocationmanager/authorizationstatus-swift.property.md)
  The current authorization status for the app.
- [enum CLAuthorizationStatus](clauthorizationstatus.md)
  Constants that indicate the app’s authorization to use location services.
- [NSLocationDefaultAccuracyReduced](../BundleResources/Information-Property-List/NSLocationDefaultAccuracyReduced.md)
  A Boolean value that indicates whether the app requests reduced location accuracy by default.
- [NSLocationAlwaysAndWhenInUseUsageDescription](../BundleResources/Information-Property-List/NSLocationAlwaysAndWhenInUseUsageDescription.md)
  A message that tells the user why the app is requesting access to the user’s location information at all times.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/cllocationmanager/requesttemporaryfullaccuracyauthorization(withpurposekey:completion:))*