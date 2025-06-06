# SFSafariExtensionViewController

**Framework**: Safari Services  
**Kind**: class

The view controller for a popover associated with your app extension.

**Availability**:
- macOS 10.12+

## Declaration

```swift
@MainActor
class SFSafariExtensionViewController
```

## Mentions

- [Adjusting settings for a toolbar item](adjusting-settings-for-a-toolbar-item.md)

#### Overview

If your toolbar item has a popover, your popover view controller should be a subclass of this class. As with other macOS development, typically you want to add your own outlets and actions to the view controller, and provide an XIB file for its user interface.

Your view controller’s contents must use Auto Layout.

## Topics

### Instance Methods
- [func dismissPopover()](sfsafariextensionviewcontroller/dismisspopover.md)

## Relationships

### Inherits From
- [NSViewController](../AppKit/NSViewController.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSEditor](../AppKit/NSEditor.md)
- [NSExtensionRequestHandling](../Foundation/NSExtensionRequestHandling.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSeguePerforming](../AppKit/NSSeguePerforming.md)
- [NSStandardKeyBindingResponding](../AppKit/NSStandardKeyBindingResponding.md)
- [NSTouchBarProvider](../AppKit/NSTouchBarProvider.md)
- [NSUserActivityRestoring](../AppKit/NSUserActivityRestoring.md)
- [NSUserInterfaceItemIdentification](../AppKit/NSUserInterfaceItemIdentification.md)

## See Also

- [Using contextual menu and toolbar item keys](using-contextual-menu-and-toolbar-item-keys.md)
  Learn about adding contextual menu items and toolbar items to a Safari app extension with information property list keys.
- [Adjusting settings for a toolbar item](adjusting-settings-for-a-toolbar-item.md)
  Customize a toolbar item for your Safari app extension.
- [Adjusting settings for contextual menu items](adjusting-settings-for-contextual-menu-items.md)
  Customize contextual menu items for your Safari app extension.
- [class SFSafariToolbarItem](sfsafaritoolbaritem.md)
  A proxy for a Safari app extension toolbar item in a Safari window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/sfsafariextensionviewcontroller)*