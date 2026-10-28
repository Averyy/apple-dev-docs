# BEEmbeddedWebBrowserEngineVersion

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

A string version number for the alternative browser engine that your app embeds.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Details

- **Name**: `BEEmbeddedWebBrowserEngineVersion`
- **Type**: string

## Discussion

If your app isn’t a browser app, but embeds an alternative browser engine, add this property to your app’s target in Xcode and set the value to the version of the alternative browser engine you use.

Supply a version that matches this regular expression: `(v(ersion)?\s?)?\d+(\.\d+)*`.

For more information, see [Creating browser extensions in Xcode](../../BrowserEngineKit/creating-browser-extensions-in-xcode.md).

## See Also

### Alternative browser engines
- [BEEmbeddedWebBrowserEngine](./beembeddedwebbrowserengine.md)
  A string name of the alternative browser engine that your app embeds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/beembeddedwebbrowserengineversion)*