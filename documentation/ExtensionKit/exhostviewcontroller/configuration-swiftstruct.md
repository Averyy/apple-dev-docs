# EXHostViewController.Configuration

**Framework**: ExtensionKit  
**Kind**: struct

An object that holds configuration options for a host view controller.

**Availability**:
- macOS 13.0+

## Declaration

```swift
struct Configuration
```

## Topics

### Creating a Configuration Object
- [init(appExtension: AppExtensionIdentity, sceneID: String)](exhostviewcontroller/configuration-swift.struct/init(appextension:sceneid:).md)
  Creates a new configuration object.
### Identifying the Extension
- [var appExtension: AppExtensionIdentity](exhostviewcontroller/configuration-swift.struct/appextension.md)
  The app extension for this configuration object.
- [var sceneID: String](exhostviewcontroller/configuration-swift.struct/sceneid.md)
  The unique identifier for this configuration object’s user interface.

## See Also

- [var configuration: EXHostViewController.Configuration?](exhostviewcontroller/configuration-swift.property.md)
  The view controller’s configuration.
- [var placeholderView: NSView](exhostviewcontroller/placeholderview.md)
  A view that’s used when the view controller has no content to display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/extensionkit/exhostviewcontroller/configuration-swift.struct)*