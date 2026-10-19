# UIApplication.LaunchOptionsKey

**Framework**: UIKit  
**Kind**: struct

The keys you use to access values in the launch options dictionary that the system passes to your app at initialization.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
struct LaunchOptionsKey
```

#### Overview

These keys are passed to the options dictionary that’s passed to the [`application(_:willFinishLaunchingWithOptions:)`](uiapplicationdelegate/application(_:willfinishlaunchingwithoptions:).md) and [`application(_:didFinishLaunchingWithOptions:)`](uiapplicationdelegate/application(_:didfinishlaunchingwithoptions:).md) methods of the app delegate.

## Topics

### Creating a launch options key
- [init(rawValue: String)](uiapplication/launchoptionskey/init(rawvalue:).md)
  Creates a launch options key with the specified raw value.
### Deprecated
- [Deprecated symbols](launchoptionskey-deprecated-symbols.md)
  Review symbols that are no longer in active development, and their recommended replacements.

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [func application(UIApplication, willFinishLaunchingWithOptions: [UIApplication.LaunchOptionsKey : Any]?) -> Bool](uiapplicationdelegate/application(_:willfinishlaunchingwithoptions:).md)
  Tells the delegate that the launch process has begun.
- [func application(UIApplication, didFinishLaunchingWithOptions: [UIApplication.LaunchOptionsKey : Any]?) -> Bool](uiapplicationdelegate/application(_:didfinishlaunchingwithoptions:).md)
  Tells the delegate that the launch process is almost done and the app is almost ready to run.
- [class let didFinishLaunchingNotification: NSNotification.Name](uiapplication/didfinishlaunchingnotification.md)
  A notification that posts immediately after the app finishes launching.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplication/launchoptionskey)*