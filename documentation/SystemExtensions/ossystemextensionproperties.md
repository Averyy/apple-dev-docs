# OSSystemExtensionProperties

**Framework**: System Extensions  
**Kind**: class  
**Role**: Class

Properties that identify a specific version of a system extension.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 10.15+

## Declaration

```swift
class OSSystemExtensionProperties
```

```objc
@interface OSSystemExtensionProperties : NSObject
```

## Topics

### Identifying the Extension
- [var bundleIdentifier: String](./ossystemextensionproperties/bundleidentifier.md)
  The bundle identifier of the extension.
- [var bundleVersion: String](./ossystemextensionproperties/bundleversion.md)
  The bundle version of the extension.
- [var bundleShortVersion: String](./ossystemextensionproperties/bundleshortversion.md)
  The bundle short version string of the extension.
### Locating the Extension’s Installed Location
- [var url: URL](./ossystemextensionproperties/url.md)
  The file URL of the extension bundle.
### Instance Properties
- [var isAwaitingUserApproval: Bool](./ossystemextensionproperties/isawaitinguserapproval.md)
- [var isEnabled: Bool](./ossystemextensionproperties/isenabled.md)
- [var isUninstalling: Bool](./ossystemextensionproperties/isuninstalling.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Handling Indeterminate Installs
- [func requestNeedsUserApproval(OSSystemExtensionRequest)](./ossystemextensionrequestdelegate/requestneedsuserapproval%28_%29.md)
  Tells the delegate that the user must grant approval before the manager can activate the extension.
- [func request(OSSystemExtensionRequest, actionForReplacingExtension: OSSystemExtensionProperties, withExtension: OSSystemExtensionProperties) -> OSSystemExtensionRequest.ReplacementAction](./ossystemextensionrequestdelegate/request%28_,actionforreplacingextension,withextension%29.md)
  Tells the delegate that the user has a different version of the extension installed on their system.
- [OSSystemExtensionRequest.ReplacementAction](./ossystemextensionrequest/replacementaction.md)
  Actions for describing how the extension manager should resolve a version conflict.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemextensions/ossystemextensionproperties)*