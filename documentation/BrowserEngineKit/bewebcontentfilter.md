# BEWebContentFilter

**Framework**: BrowserEngineKit  
**Kind**: class

An object that represents a web content filter.

**Availability**:
- iOS 26.2+
- iPadOS 26.2+

## Declaration

```swift
class BEWebContentFilter
```

## Topics

### Managing URL blocking
- [func allow(URL, completionHandler: (Bool, (any Error)?) -> Void)](bewebcontentfilter/allow(_:completionhandler:).md)
  Adds a previously blocked URL to the web content filter’s allow list.
### Evaluating URLs
- [func evaluateURL(URL, completionHandler: (Bool, Data?) -> Void)](bewebcontentfilter/evaluateurl(_:completionhandler:).md)
  Determines whether to block a URL.
- [class var shouldEvaluateURLs: Bool](bewebcontentfilter/shouldevaluateurls.md)
  Determines whether the built-in web content filter is active.
### Instance Methods
- [func evaluateURL(URL, mainFrameURL: URL, isMainFrame: Bool, completionHandler: (Bool, Data?) -> Void)](bewebcontentfilter/evaluateurl(_:mainframeurl:ismainframe:completionhandler:).md)
- [func requestPermission(for: URL, referrerURL: URL?, presenting: UIView?, completionHandler: (BEWebContentFilter.PermissionDecision, (any Error)?) -> Void)](bewebcontentfilter/requestpermission(for:referrerurl:presenting:completionhandler:).md)
### Enumerations
- [BEWebContentFilter.PermissionDecision](bewebcontentfilter/permissiondecision.md)

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

- [enum ProcessCapability](processcapability.md)
  Capabilities of a helper extension process.
- [class BEProcessCapability](beprocesscapability-76ijx.md)
  Capabilities of a helper extension process.
- [struct MediaEnvironment](mediaenvironment.md)
  An object that identifies a media playback or streaming environment.
- [class BEMediaEnvironment](bemediaenvironment-15xci.md)
  An object that identifies a media playback or streaming environment.
- [enum RenderingExtensionFeature](renderingextensionfeature.md)
  Features of a rendering extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/bewebcontentfilter)*