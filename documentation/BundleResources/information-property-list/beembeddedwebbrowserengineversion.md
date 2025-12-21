# BEEmbeddedWebBrowserEngineVersion

**Framework**: Bundle Resources  
**Kind**: typealias

A string version number for the alternative browser engine that your app embeds.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

#### Discussion

If your app isn’t a browser app, but embeds an alternative browser engine, add this property to your app’s target in Xcode and set the value to the version of the alternative browser engine you use.

Supply a version that matches this regular expression: `(v(ersion)?\s?)?\d+(\.\d+)*`.

For more information, see [`Creating browser extensions in Xcode`](https://developer.apple.com/documentation/BrowserEngineKit/creating-browser-extensions-in-xcode).

## See Also

- [BEEmbeddedWebBrowserEngine](information-property-list/beembeddedwebbrowserengine.md)
  A string name of the alternative browser engine that your app embeds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/beembeddedwebbrowserengineversion)*