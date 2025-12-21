# hostViewControllerWillDeactivate(_:error:)

**Framework**: ExtensionKit  
**Kind**: method

Tells the host that the app extension disconnected and is no longer available.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 13.0+

## Declaration

```swift
@MainActor
optional func hostViewControllerWillDeactivate(_ viewController: EXHostViewController, error: (any Error)?)
```

## Mentions

- [Including extension-based UI in your interface](including-extension-based-ui-in-your-interface.md)

#### Discussion

The host view controller calls this method when the app extension exits or when you change the view controller’s [`configuration`](exhostviewcontroller/configuration-swift.property.md) property. Use this method to close out the previous connection to the app extension.

## Parameters

- `viewController`: The host view controller that initiated the connection.
- `error`: An error object indicating why the app extension disconnected, or   if the extension exited without issues.

## See Also

- [func hostViewControllerDidActivate(EXHostViewController)](exhostviewcontrollerdelegate/hostviewcontrollerdidactivate(_:).md)
  Tells the host that the app extension is active and ready to accept an XPC connection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/extensionkit/exhostviewcontrollerdelegate/hostviewcontrollerwilldeactivate(_:error:))*