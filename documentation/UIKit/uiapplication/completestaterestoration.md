# completeStateRestoration()

**Framework**: UIKit  
**Kind**: method

Tells the app that your code has finished any asynchronous state restoration.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func completeStateRestoration()
```

#### Discussion

UIKit restores your app’s state synchronously on the main thread. If you choose to perform additional state restoration on a secondary thread, call the [`extendStateRestoration()`](uiapplication/extendstaterestoration().md) method to inform UIKit of that fact. Call this method after you finish with your background work to let the system know that state restoration is complete.

## See Also

- [func extendStateRestoration()](uiapplication/extendstaterestoration.md)
  Tells the app that your code is restoring state asynchronously.
- [func ignoreSnapshotOnNextApplicationLaunch()](uiapplication/ignoresnapshotonnextapplicationlaunch.md)
  Prevents the app from using the recent snapshot image during the next launch cycle.
- [class func registerObject(forStateRestoration: any UIStateRestoring, restorationIdentifier: String)](uiapplication/registerobject(forstaterestoration:restorationidentifier:).md)
  Registers a custom object for use with the state restoration system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplication/completestaterestoration())*