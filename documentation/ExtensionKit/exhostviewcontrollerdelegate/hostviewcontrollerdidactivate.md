# hostViewControllerDidActivate(_:)

**Framework**: ExtensionKit  
**Kind**: method

A delegate method the view controller calls when a connection succeeds.

**Availability**:
- macOS 13.0+

## Declaration

```swift
@MainActor
optional func hostViewControllerDidActivate(_ viewController: EXHostViewController)
```

#### Discussion

This delegate method gets called when the extension process has launched and the remote scene connects. After this delegate method gets called the host view controller can establish an XPC connection with the scene in the extension process.

## Parameters

- `viewController`: The user interface object from the remote process.

## See Also

- [func hostViewControllerWillDeactivate(EXHostViewController, error: (any Error)?)](exhostviewcontrollerdelegate/hostviewcontrollerwilldeactivate(_:error:).md)
  A delegate method the host view controller calls when an extension disconnects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/extensionkit/exhostviewcontrollerdelegate/hostviewcontrollerdidactivate(_:))*