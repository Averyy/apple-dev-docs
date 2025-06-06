# registryDidChangeNotification

**Framework**: AppKit  
**Kind**: property

Posted whenever the image representation class registry changes.

**Availability**:
- macOS ?+

## Declaration

```swift
class let registryDidChangeNotification: NSNotification.Name
```

#### Discussion

The notification object is the image class that is registered or unregistered. This notification does not contain a `userInfo` dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimagerep/registrydidchangenotification)*