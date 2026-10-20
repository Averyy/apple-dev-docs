# SFSafariExtensionViewController

**Framework**: Safari Services  
**Kind**: class  
**Role**: Class

The view controller for a popover associated with your app extension.

**Availability**:
- macOS 10.12+

## Declaration

```swift
class SFSafariExtensionViewController
```

```objc
@interface SFSafariExtensionViewController : NSViewController
```

## Mentions

- [Adjusting settings for a toolbar item](./adjusting-settings-for-a-toolbar-item.md)

#### Overview

If your toolbar item has a popover, your popover view controller should be a subclass of this class. As with other macOS development, typically you want to add your own outlets and actions to the view controller, and provide an XIB file for its user interface.

Your view controller’s contents must use Auto Layout.

## Topics

### Instance Methods
- [func dismissPopover()](./sfsafariextensionviewcontroller/dismisspopover%28%29.md)

## Relationships

### Inherits From
- [NSViewController](../AppKit/nsviewcontroller.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSEditor](../AppKit/nseditor.md)
- [NSExtensionRequestHandling](../Foundation/nsextensionrequesthandling.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSeguePerforming](../AppKit/nssegueperforming.md)
- [NSStandardKeyBindingResponding](../AppKit/nsstandardkeybindingresponding.md)
- [NSTouchBarProvider](../AppKit/nstouchbarprovider.md)
- [NSUserActivityRestoring](../AppKit/nsuseractivityrestoring.md)
- [NSUserInterfaceItemIdentification](../AppKit/nsuserinterfaceitemidentification.md)

## See Also

### Contextual menu and toolbar items
- [Using contextual menu and toolbar item keys](./using-contextual-menu-and-toolbar-item-keys.md)
  Learn about adding contextual menu items and toolbar items to a Safari app extension with information property list keys.
- [Adjusting settings for a toolbar item](./adjusting-settings-for-a-toolbar-item.md)
  Customize a toolbar item for your Safari app extension.
- [Adjusting settings for contextual menu items](./adjusting-settings-for-contextual-menu-items.md)
  Customize contextual menu items for your Safari app extension.
- [class SFSafariToolbarItem](./sfsafaritoolbaritem.md)
  A proxy for a Safari app extension toolbar item in a Safari window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/sfsafariextensionviewcontroller)*