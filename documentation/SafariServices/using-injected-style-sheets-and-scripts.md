# Using injected style sheets and scripts

**Framework**: Safari Services

Learn how you can affect the appearance or behavior of a webpage by using injected style sheets and scripts.

#### Overview

To add or override styles and behaviors in a webpage, you write style sheets and scripts that you then inject into your webpage to read and modify its content.

##### Add Injected Style Sheets

Injected style sheets function like user style sheets, as defined by the [`W3C`](https://developer.apple.comhttps://www.w3.org). The system adds styles in the following order:

1. Your Safari app extension styles
2. The webpage author’s styles
3. The webpage author’s styles that are declared as `!important`
4. Your Safari app extension styles that are declared as `!important`

At each stage, a new definition overrides any previous definition. The system adds style properties in your injected style sheets to existing page style properties, but your styles don’t override existing page styles unless you declare the new ones as `!important`.

For example, adding the following styles overrides a website using color text on a color background, and sets it to black text on a white background for a particular element:

```other
span.anElement {
    color:black;
    background:white;
}
```

##### Add Injected Scripts

You can inject `.js` files (text files that contain JavaScript functions and commands) into a webpage. The scripts in these files have access to the DOM of the webpages you inject them into. They have the same access privileges as scripts that execute from a webpage’s host. Injected scripts load each time a webpage loads, so keep them lightweight.

The system injects scripts into the top-level page and any subpages with HTML sources, such as iframes. Don’t assume that there’s only one instance of your script per browser tab. If you don’t want your injected script to execute inside iframes, preface your high-level functions with a test, as the following example shows:

```javascript
if (window.top === window) {
    // The containing frame is the top-level frame, not an iframe.
    // All non-iframe code goes before the closing brace.
}
```

Injected scripts have an implied namespace — you don’t have to worry about your variable or function names conflicting with those of the website author, nor can a website author call functions in your extension. In other words, injected scripts and scripts that you include in the webpage run in isolated worlds, with no access to each other’s functions or data.

## See Also

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
- [class SFSafariPageProperties](sfsafaripageproperties.md)
  An object that captures information about a webpage.
- [protocol SFSafariExtensionHandling](sfsafariextensionhandling.md)
  A protocol for implementing event handling in a Safari app extension.
- [let SFExtensionProfileKey: String](sfextensionprofilekey.md)
  A string the system uses as a key in a user info dictionary to identify a profile identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/using-injected-style-sheets-and-scripts)*