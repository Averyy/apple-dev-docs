# NSExtensionHostWillEnterForeground

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

Posted when the extension’s host app begins running in the foreground.

**Availability**:
- iOS 8.2+
- iPadOS 8.2+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static let NSExtensionHostWillEnterForeground: NSNotification.Name
```

```c
extern NSString * const NSExtensionHostWillEnterForegroundNotification;
```

## Discussion

Extensions can use this notification to restart tasks that it stopped when they moved to the background. The `object` parameter contains the `NSExtensionContext` object. This notification does not contain a `userInfo` dictionary.

## See Also

### Working with notifications
- [static let NSExtensionHostDidBecomeActive: NSNotification.Name](./nsextensionhostdidbecomeactive.md)
  Posted when the extension’s host app moves from the inactive to the active state.
- [static let NSExtensionHostWillResignActive: NSNotification.Name](./nsextensionhostwillresignactive.md)
  Posted when the extension’s host app moves from the active to the inactive state.
- [static let NSExtensionHostDidEnterBackground: NSNotification.Name](./nsextensionhostdidenterbackground.md)
  Posted when the extension’s host app begins running in the background.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsnotification/name-swift.struct/nsextensionhostwillenterforeground)*