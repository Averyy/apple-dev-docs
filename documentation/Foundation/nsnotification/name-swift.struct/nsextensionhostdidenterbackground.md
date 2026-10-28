# NSExtensionHostDidEnterBackground

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

Posted when the extension’s host app begins running in the background.

**Availability**:
- iOS 8.2+
- iPadOS 8.2+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static let NSExtensionHostDidEnterBackground: NSNotification.Name
```

```c
extern NSString * const NSExtensionHostDidEnterBackgroundNotification;
```

## Discussion

Extensions can use this notification to stop tasks and prepare the extension to be suspended. The `object` parameter contains the `NSExtensionContext` object. This notification does not contain a `userInfo` dictionary.

Extensions receive only a short amount of time to perform any background work. If you need more time to complete critical tasks, use the methods of the [`ProcessInfo`](../../processinfo.md) class to request that time.

## See Also

### Working with notifications
- [static let NSExtensionHostDidBecomeActive: NSNotification.Name](./nsextensionhostdidbecomeactive.md)
  Posted when the extension’s host app moves from the inactive to the active state.
- [static let NSExtensionHostWillResignActive: NSNotification.Name](./nsextensionhostwillresignactive.md)
  Posted when the extension’s host app moves from the active to the inactive state.
- [static let NSExtensionHostWillEnterForeground: NSNotification.Name](./nsextensionhostwillenterforeground.md)
  Posted when the extension’s host app begins running in the foreground.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsnotification/name-swift.struct/nsextensionhostdidenterbackground)*