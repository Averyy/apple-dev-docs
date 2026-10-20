# UIApplication.LaunchOptionsKey

**Framework**: UIKit  
**Kind**: struct  
**Role**: Structure

The keys you use to access values in the launch options dictionary that the system passes to your app at initialization.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
struct LaunchOptionsKey
```

```c
typedef NSString * UIApplicationLaunchOptionsKey;
```

#### Overview

These keys are passed to the options dictionary that’s passed to the [`application(_:willFinishLaunchingWithOptions:)`](../uiapplicationdelegate/application%28_,willfinishlaunchingwithoptions%29.md) and [`application(_:didFinishLaunchingWithOptions:)`](../uiapplicationdelegate/application%28_,didfinishlaunchingwithoptions%29.md) methods of the app delegate.

## Topics

### Creating a launch options key
- [init(rawValue: String)](./launchoptionskey/init%28rawvalue%29.md)
  Creates a launch options key with the specified raw value.
### Deprecated
- [Deprecated symbols](../launchoptionskey-deprecated-symbols.md)
  Review symbols that are no longer in active development, and their recommended replacements.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Initializing the app
- [func application(UIApplication, willFinishLaunchingWithOptions: [UIApplication.LaunchOptionsKey : Any]?) -> Bool](../uiapplicationdelegate/application%28_,willfinishlaunchingwithoptions%29.md)
  Tells the delegate that the launch process has begun.
- [func application(UIApplication, didFinishLaunchingWithOptions: [UIApplication.LaunchOptionsKey : Any]?) -> Bool](../uiapplicationdelegate/application%28_,didfinishlaunchingwithoptions%29.md)
  Tells the delegate that the launch process is almost done and the app is almost ready to run.
- [class let didFinishLaunchingNotification: NSNotification.Name](./didfinishlaunchingnotification.md)
  A notification that posts immediately after the app finishes launching.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplication/launchoptionskey)*