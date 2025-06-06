# ignoreSnapshotOnNextApplicationLaunch()

**Framework**: UIKit  
**Kind**: method

Prevents the app from using the recent snapshot image during the next launch cycle.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func ignoreSnapshotOnNextApplicationLaunch()
```

#### Discussion

As part of the state preservation process, UIKit captures your app’s user interface and stores it in an image file. When your app is relaunched, the system displays this snapshot image in place of your app’s default launch image to preserve the notion that your app was still running. If you feel that the snapshot cannot correctly reflect your app’s user interface when your app is relaunched, call this method to let UIKit know that it should use your app’s default launch image instead of the snapshot.

You must call this method from within the code you use to preserve your app’s state.

## See Also

- [func extendStateRestoration()](uiapplication/extendstaterestoration.md)
  Tells the app that your code is restoring state asynchronously.
- [func completeStateRestoration()](uiapplication/completestaterestoration.md)
  Tells the app that your code has finished any asynchronous state restoration.
- [class func registerObject(forStateRestoration: any UIStateRestoring, restorationIdentifier: String)](uiapplication/registerobject(forstaterestoration:restorationidentifier:).md)
  Registers a custom object for use with the state restoration system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplication/ignoresnapshotonnextapplicationlaunch())*