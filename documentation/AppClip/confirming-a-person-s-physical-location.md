# Confirming a person’s physical location

**Framework**: App Clips

Add code to quickly confirm a person’s physical location while respecting their privacy.

#### Overview

If you create an App Clip that people invoke at a physical location, you may need to confirm a person’s location before allowing them to perform a task. For a quick launch and to preserve user privacy, App Clips use a lightweight mechanism in which the system verifies that a person is at a specific, expected location. When you adopt this mechanism, and when people allow it, the  contains a note that tells people that the App Clip can verify their location. They can disable location verification by tapping the note on the App Clip card.

![An App Clip card for an App Clip that can verify a person’s physical location.](https://docs-assets.developer.apple.com/published/7486feb43af39b75207a8b25924d5f1e/media-3669502%402x.png)

##### Enable Your App Clip to Verify a Persons Location

To enable your App Clip to verify the person’s location, modify your App Clip’s `Info.plist` file:

1. Open your App Clip’s `Info.plist`, add the [`NSAppClip`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSAppClip) key, and set its type to `Dictionary`.
2. Add an entry to the dictionary with [`NSAppClipRequestLocationConfirmation`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSAppClip/NSAppClipRequestLocationConfirmation) as the key, select `Boolean` as its type, and set its value to `true`.

![An Info.plist file with the entry that allows the App Clip to confirm a person’s location.](https://docs-assets.developer.apple.com/published/cf62aa4d7db12b981dcb81f978456f7b/media-3975648%402x.png)

Alternatively, open the `Info.plist` file in the property list editor and add the entry by selecting App Clip from the list of keys. This adds the [`NSAppClip`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSAppClip) key and the following entries of type `Boolean` to its dictionary: “Requests ephemeral user notifications” and “Requests location confirmation.” Per default, the value for both entries is `NO`. Change the value for “Requests location confirmation” to `YES`.

> **Note**:  Don’t add an entry for the [`NSAppClipRequestLocationConfirmation`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSAppClip/NSAppClipRequestLocationConfirmation) key to your full app’s `Info.plist` — functionality to confirm a person’s location is only available to App Clips. Instead, modify your full app’s code to request permission to access the location of a device and make use of the [`Core Location`](https://developer.apple.com/documentation/CoreLocation) framework. For more information, see [`Getting the current location of a device`](https://developer.apple.com/documentation/CoreLocation/getting-the-current-location-of-a-device).

 Don’t add an entry for the [`NSAppClipRequestLocationConfirmation`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSAppClip/NSAppClipRequestLocationConfirmation) key to your full app’s `Info.plist` — functionality to confirm a person’s location is only available to App Clips. Instead, modify your full app’s code to request permission to access the location of a device and make use of the [`Core Location`](https://developer.apple.com/documentation/CoreLocation) framework. For more information, see [`Getting the current location of a device`](https://developer.apple.com/documentation/CoreLocation/getting-the-current-location-of-a-device).

##### Add Code That Verifies the Physical Location

After you modify your App Clip’s `Info.plist` file, add code to provide the expected physical location information to the App Clip. To retrieve this information, encode an identifier in the URL that launches the App Clip, and use the identifier to look up the location information for a business in your database. Alternatively, encode the location information in the URL that launches the App Clip.

On launch, access the location information, use it to create a [`CLCircularRegion`](https://developer.apple.com/documentation/CoreLocation/CLCircularRegion) object with a radius of up to 500 meters, and pass it to the [`confirmAcquired(in:completionHandler:)`](apactivationpayload/confirmacquired(in:completionhandler:).md) function.

The following code verifies a person’s location when they launch the App Clip. Make sure to update your user interface for each possible result, including the case where a person denies access to location services on their device.

```swift
import UIKit
import AppClip
import CoreLocation

class SceneDelegate: UIResponder, UIWindowSceneDelegate {
    
    var window: UIWindow?
    
    // Call the verifyUserLocation(_:) function in all applicable lifecycle callbacks.

    func verifyUserLocation(_ activity: NSUserActivity?) {
        
        // Guard against faulty data.
        guard activity != nil else { return }
        guard activity!.activityType == NSUserActivityTypeBrowsingWeb else { return }
        guard let payload = activity!.appClipActivationPayload else { return }
        guard let incomingURL = activity?.webpageURL else { return }

        // Create a CLRegion object.
        guard let region = location(from: incomingURL) else {
            // Respond to parsing errors here.
            return
        }
        
        // Verify that the invocation happened at the expected location.
        payload.confirmAcquired(in: region) { (inRegion, error) in
            guard let confirmationError = error as? APActivationPayloadError else {
                if inRegion {
                    // The location of the NFC tag matches a person's location.
                } else {
                    // The location of the NFC tag doesn't match the records,
                    // for example, if someone moved the NFC tag.
                }
                return
            }
            
            if confirmationError.code == .doesNotMatch {
                // The scanned URL isn't registered for the App Clip.
            } else {
                // A person denied location access, or the source of the
                // App Clip’s invocation isn't an NFC tag or visual code.
            }
        }
    }

    func location(from url:URL) -> CLRegion? {
        let coordinates = CLLocationCoordinate2D(latitude: 37.334722,
                                                 longitude: 122.008889)
        return CLCircularRegion(center: coordinates,
                                radius: 100,
                                identifier: "Apple Park")
    }
}
```

For more information on how you can access the App Clip’s invocation URL, see [`Responding to invocations`](responding-to-invocations.md).

## See Also

- [Configuring the launch experience of your App Clip](configuring-the-launch-experience-of-your-app-clip.md)
  Review how people launch your App Clip, identify invocation URLs, make use of default App Clip links, and configure experiences in App Store Connect.
- [Associating your App Clip with your website](associating-your-app-clip-with-your-website.md)
  Enable the system to verify your App Clip to support invocations in iOS 16.3 or earlier and from your website.
- [Supporting invocations from your website and the Messages app](supporting-invocations-from-your-website-and-the-messages-app.md)
  Display a Smart App Banner and the App Clip card on your website that people tap to launch your App Clip, and add support for invocations from the Messages app.
- [Responding to invocations](responding-to-invocations.md)
  Add code to respond to invocations and offer a focused launch experience.
- [Launching another app’s App Clip from your app](launching-another-app-s-app-clip-from-your-app.md)
  Enable people to launch another app’s App Clip from your app with App Clip links and offer a rich preview of it with the Link Presentation framework.
- [class APActivationPayload](apactivationpayload.md)
  Information that’s passed to an App Clip on launch.
- [NSAppClip](../BundleResources/Information-Property-List/NSAppClip.md)
  A collection of keys that an App Clip uses to get additional capabilities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appclip/confirming-a-person-s-physical-location)*