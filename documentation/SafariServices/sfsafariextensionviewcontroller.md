# SFSafariExtensionViewController

**Framework**: Safari Services  
**Kind**: class

The view controller for a popover associated with your app extension.

**Availability**:
- macOS 10.12+

## Declaration

```swift
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
- [NSViewController](../appkit/nsviewcontroller.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSEditor](../appkit/nseditor.md)
- [NSExtensionRequestHandling](../foundation/nsextensionrequesthandling.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSeguePerforming](../appkit/nssegueperforming.md)
- [NSStandardKeyBindingResponding](../appkit/nsstandardkeybindingresponding.md)
- [NSTouchBarProvider](../appkit/nstouchbarprovider.md)
- [NSUserActivityRestoring](../appkit/nsuseractivityrestoring.md)
- [NSUserInterfaceItemIdentification](../appkit/nsuserinterfaceitemidentification.md)

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