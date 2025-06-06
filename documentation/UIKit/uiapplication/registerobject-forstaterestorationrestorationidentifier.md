# registerObject(forStateRestoration:restorationIdentifier:)

**Framework**: UIKit  
**Kind**: method

Registers a custom object for use with the state restoration system.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class func registerObject(forStateRestoration object: any UIStateRestoring, restorationIdentifier: String)
```

## Mentions

- [About the UI preservation process](about-the-ui-preservation-process.md)

#### Discussion

You use this method to register objects that you want to save as part of the overall state restoration process. Registering the object makes it available for inclusion in the restoration archive but does not automatically include it. To include the object, refer to it from one of your other interface objects. For example, you might write out a reference to the object from the [`encodeRestorableState(with:)`](uiviewcontroller/encoderestorablestate(with:).md) method of one of your view controllers.

## Parameters

- `object`: The object to be registered with the restoration archive. The object must adopt the   protocol. This parameter must not be  .
- `restorationIdentifier`: The restoration identifier for the object. UIKit uses this parameter to distinguish the object from other objects in the archive. This parameter must not be  .

## See Also

- [func extendStateRestoration()](uiapplication/extendstaterestoration.md)
  Tells the app that your code is restoring state asynchronously.
- [func completeStateRestoration()](uiapplication/completestaterestoration.md)
  Tells the app that your code has finished any asynchronous state restoration.
- [func ignoreSnapshotOnNextApplicationLaunch()](uiapplication/ignoresnapshotonnextapplicationlaunch.md)
  Prevents the app from using the recent snapshot image during the next launch cycle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplication/registerobject(forstaterestoration:restorationidentifier:))*