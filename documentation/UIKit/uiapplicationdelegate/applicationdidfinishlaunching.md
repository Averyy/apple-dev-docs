# applicationDidFinishLaunching(_:)

**Framework**: UIKit  
**Kind**: method

Tells the delegate when the app has finished launching.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func applicationDidFinishLaunching(_ application: UIApplication)
```

#### Discussion

Don’t use this method in your apps; instead, use the [`application(_:willFinishLaunchingWithOptions:)`](uiapplicationdelegate/application(_:willfinishlaunchingwithoptions:).md) and [`application(_:didFinishLaunchingWithOptions:)`](uiapplicationdelegate/application(_:didfinishlaunchingwithoptions:).md) methods.

Your implementation of this method creates your app’s user interface and initializes the app’s data structures. If your app persists its state between launches, you would also use this method to restore your app to its previous state.

After calling this method, the app also posts a [`didFinishLaunchingNotification`](uiapplication/didfinishlaunchingnotification.md) notification to give interested objects a chance to respond to the initialization cycle.

## Parameters

- `application`: The singleton app object.

## See Also

- [Deprecated symbols](uiapplicationdelegate-deprecated-symbols.md)
  Symbols that are no longer supported.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/applicationdidfinishlaunching(_:))*