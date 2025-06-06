# Suspending authorization requests

**Framework**: Core Location

Defer the system’s authorization request dialog until your app is ready.

#### Overview

If your app has an onboarding flow that includes obtaining location updates, you may want to defer the Core Location’s request for authorization from the user. You can inhibit the auto-prompting in your app by creating a [`CLServiceSession`](clservicesession-pt7n.md) at a convenient time in your app, then iterating over its diagnostics property to determine the level of authorization the person using your app selects. The following code snippet demonstrates how to defer the prompting.

```swift
func doPromptingFlow() async {
    await showHelloPrompt()

    // Obtain a session. This causes Core Location to display the authorization prompt.
    let session = CLServiceSession.session(authorization: .whenInUse)

    // Wait for interaction with the prompot to complete (successfully or with denial).
    for try await diagnostic in session.diagnostics {
        if !diagnostic.authorizationRequestInProgress {
            // A denial occurred.
            break
        }
    }

    await doFurtherWork()
}
```

Add the `CLRequireExplicitServiceSession` property to your app’s Info.plist file to opt into this control behavior.

## See Also

- [Requesting authorization to use location services](requesting-authorization-to-use-location-services.md)
  Obtain authorization to use location services and manage changes to your app’s authorization status.
- [enum CLAuthorizationStatus](clauthorizationstatus.md)
  Constants that indicate the app’s authorization to use location services.
- [enum CLAccuracyAuthorization](claccuracyauthorization.md)
  Constants that indicate the level of location accuracy the app has authorization to use.
- [NSLocationAlwaysAndWhenInUseUsageDescription](../BundleResources/Information-Property-List/NSLocationAlwaysAndWhenInUseUsageDescription.md)
  A message that tells the user why the app is requesting access to the user’s location information at all times.
- [NSLocationWhenInUseUsageDescription](../BundleResources/Information-Property-List/NSLocationWhenInUseUsageDescription.md)
  A message that tells the user why the app is requesting access to the user’s location information while the app is running in the foreground.
- [NSLocationUsageDescription](../BundleResources/Information-Property-List/NSLocationUsageDescription.md)
  A message that tells the user why the app is requesting access to the user’s location information.
- [NSLocationDefaultAccuracyReduced](../BundleResources/Information-Property-List/NSLocationDefaultAccuracyReduced.md)
  A Boolean value that indicates whether the app requests reduced location accuracy by default.
- [NSLocationAlwaysUsageDescription](../BundleResources/Information-Property-List/NSLocationAlwaysUsageDescription.md)
  A message that tells the user why the app is requesting access to the user’s location at all times.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/suspending-authorization-requests)*