# autosavesConfiguration

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the toolbar autosaves its configuration.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS

## Declaration

```swift
var autosavesConfiguration: Bool { get set }
```

```objc
@property BOOL autosavesConfiguration;
```

#### Discussion

When the value of this property is [`true`](../../Swift/true.md), the toolbar automatically writes any configuration changes to user defaults. It associates the configuration details with the value in its identifier property. If mutliple toolbars share the same identifier, they all share the same configuration settings. When the value of this property is [`false`](../../Swift/false.md), the toolbar doesn’t save changes and reverts to the default configuration when the app relaunches.

The default of this property is [`false`](../../Swift/false.md).

> ❗ **Important**:  If you allow people to customize your app’s toolbars, enable this property to save the changes they make. Alternatively, use the [`configuration`](./configuration.md) property and [`setConfiguration(_:)`](./setconfiguration%28_%29.md) method to manage the autosave process yourself.

## See Also

### Related Documentation
- [var allowsUserCustomization: Bool](./allowsusercustomization.md)
  A Boolean value that indicates whether users can modify the contents of the toolbar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstoolbar/autosavesconfiguration)*