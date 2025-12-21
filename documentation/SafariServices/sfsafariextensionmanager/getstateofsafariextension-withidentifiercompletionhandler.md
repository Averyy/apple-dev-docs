# getStateOfSafariExtension(withIdentifier:completionHandler:)

**Framework**: Safari Services  
**Kind**: method

Returns the current state of a Safari extension.

**Availability**:
- macOS 10.12+

## Declaration

```swift
class func stateOfSafariExtension(withIdentifier identifier: String) async throws -> SFSafariExtensionState
```

#### Discussion

Use this method to check on the state of one of the Safari app or web extensions embedded inside your app.

## Parameters

- `identifier`: The bundle identifier for the Safari extension to check.
- `completionHandler`: The completion handler the system calls with either the extension’s state or an error.

## See Also

- [class func getStateOfExtension(withIdentifier: String, completionHandler: (SFSafariExtensionState?, (any Error)?) -> Void)](sfsafariextensionmanager/getstateofextension(withidentifier:completionhandler:).md)
  Returns the current state of a Safari web extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/sfsafariextensionmanager/getstateofsafariextension(withidentifier:completionhandler:))*