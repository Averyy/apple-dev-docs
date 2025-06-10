# hostViewControllerWillDeactivate(_:error:)

**Framework**: ExtensionKit  
**Kind**: method

A delegate method the host view controller calls when an extension disconnects.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 13.0+

## Declaration

```swift
@MainActor
optional func hostViewControllerWillDeactivate(_ viewController: EXHostViewController, error: (any Error)?)
```

#### Discussion

Called when the host view controller stops hosting the remote user interface. This can occur when the extension exits or when the view controller’s configuration property changes.

## Parameters

- `viewController`: The view controller for the extension that’s disconnecting
- `error`: An error object containing information about why the object disconnected, or   if it’s disconnecting without error.

## See Also

- [func hostViewControllerDidActivate(EXHostViewController)](exhostviewcontrollerdelegate/hostviewcontrollerdidactivate(_:).md)
  A delegate method the view controller calls when a connection succeeds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/extensionkit/exhostviewcontrollerdelegate/hostviewcontrollerwilldeactivate(_:error:))*