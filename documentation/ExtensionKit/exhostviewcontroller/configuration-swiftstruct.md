# EXHostViewController.Configuration

**Framework**: ExtensionKit  
**Kind**: struct

An object that holds configuration options for a host view controller.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 13.0+

## Declaration

```swift
struct Configuration
```

## Topics

### Creating a configuration type
- [init(appExtension: AppExtensionIdentity, sceneID: String)](exhostviewcontroller/configuration-swift.struct/init(appextension:sceneid:).md)
  Creates a new configuration object.
### Identifying the scene to display
- [var appExtension: AppExtensionIdentity](exhostviewcontroller/configuration-swift.struct/appextension.md)
  The app extension for this configuration object.
- [var sceneID: String](exhostviewcontroller/configuration-swift.struct/sceneid.md)
  The unique identifier for this configuration object’s user interface.

## See Also

- [var configuration: EXHostViewController.Configuration?](exhostviewcontroller/configuration-swift.property.md)
  The information the host view controller uses to fetch the appropriate scene from an app extension.
- [var placeholderView: UIView](exhostviewcontroller/placeholderview.md)
  The view to display when the view controller has no app extension content to display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/extensionkit/exhostviewcontroller/configuration-swift.struct)*