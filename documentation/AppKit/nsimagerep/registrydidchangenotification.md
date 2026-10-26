# registryDidChangeNotification

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

Posted whenever the image representation class registry changes.

**Availability**:
- macOS

## Declaration

```swift
class let registryDidChangeNotification: NSNotification.Name
```

```c
extern NSNotificationName NSImageRepRegistryDidChangeNotification;
```

#### Discussion

The notification object is the image class that is registered or unregistered. This notification does not contain a `userInfo` dictionary.

To observe this notification using Swift concurrency, use [`NSImageRep.RegistryDidChangeMessage`](./registrydidchangemessage.md).

## See Also

### Notifications
- [NSImageRepRegistryChangedNotification](../nsimagerepregistrychangednotification.md)
  Posted whenever the image representation class registry changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimagerep/registrydidchangenotification)*