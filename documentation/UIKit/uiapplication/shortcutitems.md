# shortcutItems

**Framework**: UIKit  
**Kind**: property

The Home screen dynamic quick actions for your app; available on devices that support 3D Touch.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var shortcutItems: [UIApplicationShortcutItem]? { get set }
```

#### Discussion

Set this property to register an array of dynamic quick actions to display on the Home screen when a user presses your app icon. Read this property to retrieve the currently registered Home screen dynamic quick actions.

The items in the `shortcutItems` array are instances of the [`UIApplicationShortcutItem`](uiapplicationshortcutitem.md) class, and are therefore immutable.

> **Note**: Dynamic vs. Static Quick Actions: The items in an application object’s `shortcutItems` array, although immutable, are considered  to distinguish them from the  quick actions you can specify at build time in the [`UIApplicationShortcutItems`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Reference/InfoPlistKeyReference/Articles/iPhoneOSKeys.html#//apple_ref/doc/uid/TP40009252-SW36) array in your Xcode project’s `Info.plist` file. You create dynamic quick actions, and register them with your application object, at runtime.

The system populates the displayed set of Home screen quick actions, starting at the top, first with your static quick actions. Only if there are additional positions available does it also show your dynamic quick actions, up to the system-defined limit.

The onscreen ordering of your Home screen quick actions reflects the ordering in your [`UIApplicationShortcutItems`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Reference/InfoPlistKeyReference/Articles/iPhoneOSKeys.html#//apple_ref/doc/uid/TP40009252-SW36) array (if that array contains items) and the ordering of the items in the `shortcutItems` array (if any are displayed).

> **Note**:  When you read the value of this property, you obtain an array that contains, exclusively, your  Home screen quick actions. Any static quick actions you’ve defined are not represented in this property’s value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplication/shortcutitems)*