# getStateOfExtension(withIdentifier:completionHandler:)

**Framework**: Safari Services  
**Kind**: method

Returns the current state of a Safari web extension.

**Availability**:
- iOS 26.2+
- iPadOS 26.2+
- Mac Catalyst 26.2+
- visionOS 26.2+

## Declaration

```swift
class func stateOfExtension(withIdentifier identifier: String) async throws -> SFSafariExtensionState
```

#### Discussion

Use this method to check on the state of a Safari web extension embedded inside your app.

## Parameters

- `identifier`: The bundle identifier for the Safari web extension to check.
- `completionHandler`: The completion handler the system calls with either the extension’s state or an error.

## See Also

- [class func getStateOfSafariExtension(withIdentifier: String, completionHandler: (SFSafariExtensionState?, (any Error)?) -> Void)](sfsafariextensionmanager/getstateofsafariextension(withidentifier:completionhandler:).md)
  Returns the current state of a Safari extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/sfsafariextensionmanager/getstateofextension(withidentifier:completionhandler:))*