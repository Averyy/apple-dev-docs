# BEWebAppManifest

**Framework**: BrowserEngineKit  
**Kind**: class

An object that represents a web app manifest.

**Availability**:
- iOS 17.5+
- iPadOS 17.5+
- macOS ?+
- tvOS 17.5+
- visionOS 1.2+
- watchOS 10.5+

## Declaration

```swift
class BEWebAppManifest
```

#### Overview

To add a web app or bookmark to someone’s Home Screen:

1. Create a [`SFAddToHomeScreenActivityItem`](https://developer.apple.com/documentation/safariservices/sfaddtohomescreenactivityitem) that represents the web app or bookmark.
2. A web app indicates its manifest using a `<link/>` element with the attribute `rel=manifest`; the `href` attribute is a URL that locates the manifest JSON. If the website offers a web app manifest, initialize a `BEWebAppManifest` with the contents of the web app’s manifest.
3. Create a [`UIActivityViewController`](https://developer.apple.com/documentation/uikit/uiactivityviewcontroller) with the `SFAddToHomeScreenActivityItem` you created in step 1 in its list of activity items.
4. Present the `UIActivityViewController`.
5. When someone selects the Add to Home Screen activity, the system calls the activity item’s [`getWebAppManifest(completionHandler:)`](https://developer.apple.com/documentation/safariservices/sfaddtohomescreenactivityitem/getwebappmanifest(completionhandler:)) method. Pass the web app manifest you created in step 2 to the completion handler in your implementation, or `nil` if the website doesn’t offer a web app manifest or you can’t fetch the manifest.

## Topics

### Creating a web app manifest
- [init?(JSONData: Data, manifestURL: URL)](bewebappmanifest/init(jsondata:manifesturl:)-4zjpz.md)
- [init?(jsonData: Data, manifestURL: URL)](bewebappmanifest/init(jsondata:manifesturl:)-3azfg.md)
  Returns nil if manifestURL is invalid or jsonData cannot be parsed.
### Getting manifest information
- [var jsonData: Data](bewebappmanifest/jsondata.md)
- [var manifestURL: URL](bewebappmanifest/manifesturl.md)

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

- [View and input coordination](view-coordination.md)
  Display content in the browser’s UI that an extension renders.
- [Text interaction](text-interaction.md)
  Integrate your web browser engine asynchronously with the text system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/bewebappmanifest)*