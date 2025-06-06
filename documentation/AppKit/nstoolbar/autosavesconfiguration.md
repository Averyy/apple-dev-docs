# autosavesConfiguration

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates whether the toolbar autosaves its configuration.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS ?+

## Declaration

```swift
@MainActor
var autosavesConfiguration: Bool { get set }
```

#### Discussion

When the value of this property is [`true`](https://developer.apple.com/documentation/swift/true), the toolbar automatically writes any configuration changes to user defaults. It associates the configuration details with the value in its identifier property. If mutliple toolbars share the same identifier, they all share the same configuration settings. When the value of this property is [`false`](https://developer.apple.com/documentation/swift/false), the toolbar doesn’t save changes and reverts to the default configuration when the app relaunches.

The default of this property is [`false`](https://developer.apple.com/documentation/swift/false).

> ❗ **Important**:  If you allow people to customize your app’s toolbars, enable this property to save the changes they make. Alternatively, use the [`configuration`](nstoolbar/configuration.md) property and [`setConfiguration(_:)`](nstoolbar/setconfiguration(_:).md) method to manage the autosave process yourself.

 If you allow people to customize your app’s toolbars, enable this property to save the changes they make. Alternatively, use the [`configuration`](nstoolbar/configuration.md) property and [`setConfiguration(_:)`](nstoolbar/setconfiguration(_:).md) method to manage the autosave process yourself.

## See Also

- [var allowsUserCustomization: Bool](nstoolbar/allowsusercustomization.md)
  A Boolean value that indicates whether users can modify the contents of the toolbar.
- [var configuration: [String : Any]](nstoolbar/configuration.md)
  A dictionary containing the current configuration details for the toolbar.
- [func setConfiguration([String : Any])](nstoolbar/setconfiguration(_:).md)
  Specifies the new configuration details for the toolbar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstoolbar/autosavesconfiguration)*