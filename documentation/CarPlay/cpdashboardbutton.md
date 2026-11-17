# CPDashboardButton

**Framework**: CarPlay  
**Kind**: class  
**Role**: Class

A shortcut button for placement on the CarPlay Dashboard.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+

## Declaration

```swift
class CPDashboardButton
```

```objc
@interface CPDashboardButton : NSObject
```

## Topics

### Creating a dashboard button
- [init(titleVariants: [String], subtitleVariants: [String], image: UIImage, handler: ((CPDashboardButton) -> Void)?)](./cpdashboardbutton/init%28titlevariants,subtitlevariants,image,handler%29.md)
  Creates a dashboard button that displays a title, an optional subtitle, and an image.
- [init?(coder: NSCoder)](./cpdashboardbutton/init%28coder%29.md)
### Accessing the button configuration
- [var titleVariants: [String]](./cpdashboardbutton/titlevariants.md)
  The array of title variants for the button.
- [var subtitleVariants: [String]](./cpdashboardbutton/subtitlevariants.md)
  The array of subtitle variants for the button.
- [var image: UIImage](./cpdashboardbutton/image.md)
  The image the button displays.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Dashboard display
- [class CPDashboardController](./cpdashboardcontroller.md)
  A controller that provides shortcut buttons for the CarPlay Dashboard.
- [class CPTemplateApplicationDashboardScene](./cptemplateapplicationdashboardscene.md)
  A CarPlay scene that controls your app’s dashboard navigation window.
- [protocol CPTemplateApplicationDashboardSceneDelegate](./cptemplateapplicationdashboardscenedelegate.md)
  The methods for responding to the life-cycle events of your navigation app’s dashboard scene.
- [CPSupportsDashboardNavigationScene](../BundleResources/information-property-list/uiapplicationscenemanifest/cpsupportsdashboardnavigationscene.md)
  A Boolean value that indicates whether your app supports displaying navigation content in the CarPlay Dashboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpdashboardbutton)*