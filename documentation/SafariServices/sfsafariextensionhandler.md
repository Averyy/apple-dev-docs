# SFSafariExtensionHandler

**Framework**: Safari Services  
**Kind**: class

A base class that you subclass to handle events in your Safari app extension.

**Availability**:
- macOS 10.12+

## Declaration

```swift
class SFSafariExtensionHandler
```

## Mentions

- [Adjusting settings for contextual menu items](adjusting-settings-for-contextual-menu-items.md)
- [Building a Safari app extension](building-a-safari-app-extension.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSExtensionRequestHandling](../Foundation/NSExtensionRequestHandling.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [SFSafariExtensionHandling](sfsafariextensionhandling.md)

## See Also

- [Using injected style sheets and scripts](using-injected-style-sheets-and-scripts.md)
  Learn how you can affect the appearance or behavior of a webpage by using injected style sheets and scripts.
- [Injecting a script into a webpage](injecting-a-script-into-a-webpage.md)
  Inject a script that you write for a Safari app extension into a webpage.
- [Injecting CSS style sheets into a webpage](injecting-css-style-sheets-into-a-webpage.md)
  Add to or override styles by injecting CSS style sheets into webpages.
- [Passing messages between Safari app extensions and injected scripts](passing-messages-between-safari-app-extensions-and-injected-scripts.md)
  Communicate between your Safari app extension and injected scripts.
- [class SFSafariExtensionManager](sfsafariextensionmanager.md)
  A class that your app uses to find out the current state of a Safari extension.
- [class SFSafariExtensionState](sfsafariextensionstate.md)
  The state of a Safari extension.
- [class SFSafariPageProperties](sfsafaripageproperties.md)
  An object that captures information about a webpage.
- [protocol SFSafariExtensionHandling](sfsafariextensionhandling.md)
  A protocol for implementing event handling in a Safari app extension.
- [let SFExtensionProfileKey: String](sfextensionprofilekey.md)
  A string the system uses as a key in a user info dictionary to identify a profile identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/sfsafariextensionhandler)*