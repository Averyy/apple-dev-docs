# delegate

**Framework**: ExtensionKit  
**Kind**: property

A custom delegate object you use to receive notifications about the activation and deactivation of the app extension.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 13.0+

## Declaration

```swift
@MainActor
weak var delegate: (any EXHostViewControllerDelegate)? { get set }
```

## See Also

- [protocol EXHostViewControllerDelegate](exhostviewcontrollerdelegate.md)
  An interface you use to track the activation and deactivation of an app extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/extensionkit/exhostviewcontroller/delegate)*