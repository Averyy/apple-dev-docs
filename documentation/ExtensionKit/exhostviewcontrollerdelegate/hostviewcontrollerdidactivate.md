# hostViewControllerDidActivate(_:)

**Framework**: ExtensionKit  
**Kind**: method

Tells the host that the app extension is active and ready to accept an XPC connection.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 13.0+

## Declaration

```swift
@MainActor
optional func hostViewControllerDidActivate(_ viewController: EXHostViewController)
```

## Mentions

- [Including extension-based UI in your interface](including-extension-based-ui-in-your-interface.md)

#### Discussion

The host view controller calls this method after it launches an app extension and connects to its remote scene. Use this method to establish an XPC connection to the newly created UI instance.

## Parameters

- `viewController`: The host view controller that initiated the connection.

## See Also

- [func hostViewControllerWillDeactivate(EXHostViewController, error: (any Error)?)](exhostviewcontrollerdelegate/hostviewcontrollerwilldeactivate(_:error:).md)
  Tells the host that the app extension disconnected and is no longer available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/extensionkit/exhostviewcontrollerdelegate/hostviewcontrollerdidactivate(_:))*