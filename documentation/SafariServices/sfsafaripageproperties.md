# SFSafariPageProperties

**Framework**: Safari Services  
**Kind**: class

An object that captures information about a webpage.

**Availability**:
- macOS 10.12+

## Declaration

```swift
class SFSafariPageProperties
```

## Mentions

- [Adjusting website access permissions](adjusting-website-access-permissions.md)

#### Overview

Use the properties object to retrieve page information, such as the current URL, page title, active status, and private browsing status.

## Topics

### Getting the Safari Page Properties
- [var isActive: Bool](sfsafaripageproperties/isactive.md)
  A Boolean value that indicates whether the page is currently active.
- [var title: String?](sfsafaripageproperties/title.md)
  The title of the page.
- [var url: URL?](sfsafaripageproperties/url.md)
  Indicates the URL of the page.
- [var usesPrivateBrowsing: Bool](sfsafaripageproperties/usesprivatebrowsing.md)
  A Boolean value that indicates whether the page is using Safari Private Browsing.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Using injected style sheets and scripts](using-injected-style-sheets-and-scripts.md)
  Learn how you can affect the appearance or behavior of a webpage by using injected style sheets and scripts.
- [Injecting a script into a webpage](injecting-a-script-into-a-webpage.md)
  Inject a script that you write for a Safari app extension into a webpage.
- [Injecting CSS style sheets into a webpage](injecting-css-style-sheets-into-a-webpage.md)
  Add to or override styles by injecting CSS style sheets into webpages.
- [Passing messages between Safari app extensions and injected scripts](passing-messages-between-safari-app-extensions-and-injected-scripts.md)
  Communicate between your Safari app extension and injected scripts.
- [class SFSafariExtensionHandler](sfsafariextensionhandler.md)
  A base class that you subclass to handle events in your Safari app extension.
- [class SFSafariExtensionManager](sfsafariextensionmanager.md)
  A class that your app uses to find out the current state of a Safari extension.
- [class SFSafariExtensionState](sfsafariextensionstate.md)
  The state of a Safari extension.
- [protocol SFSafariExtensionHandling](sfsafariextensionhandling.md)
  A protocol for implementing event handling in a Safari app extension.
- [let SFExtensionProfileKey: String](sfextensionprofilekey.md)
  A string the system uses as a key in a user info dictionary to identify a profile identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/sfsafaripageproperties)*