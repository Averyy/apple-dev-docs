# configuration

**Framework**: ExtensionKit  
**Kind**: property  
**Role**: Instance Property

The information the host view controller uses to fetch the appropriate scene from an app extension.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 13.0+

## Declaration

```swift
@MainActor
@preconcurrency var configuration: EXHostViewController.Configuration? { get set }
```

## Mentions

- [Including extension-based UI in your interface](../including-extension-based-ui-in-your-interface.md)

## See Also

### Configuring the view controller
- [EXHostViewController.Configuration](./configuration-swift.struct.md)
  An object that holds configuration options for a host view controller.
- [var placeholderView: UIView](./placeholderview.md)
  The view to display when the view controller has no app extension content to display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/extensionkit/exhostviewcontroller/configuration-swift.property)*