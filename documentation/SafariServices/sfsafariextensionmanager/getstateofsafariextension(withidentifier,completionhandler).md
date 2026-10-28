# getStateOfSafariExtension(withIdentifier:completionHandler:)

**Framework**: Safari Services  
**Kind**: method  
**Role**: Type Method

Returns the current state of a Safari extension.

**Availability**:
- macOS 10.12+

## Declaration

```swift
class func getStateOfSafariExtension(withIdentifier identifier: String, completionHandler: @escaping @MainActor @Sendable (SFSafariExtensionState?, (any Error)?) -> Void)
```

```swift
class func stateOfSafariExtension(withIdentifier identifier: String) async throws -> SFSafariExtensionState
```

```objc
+ (void) getStateOfSafariExtensionWithIdentifier:(NSString *) identifier completionHandler:(void (^)(SFSafariExtensionState *, NSError *)) completionHandler;
```

## Discussion

Use this method to check on the state of one of the Safari app or web extensions embedded inside your app.

## Parameters

- `identifier`: The bundle identifier for the Safari extension to check.
- `completionHandler`: The completion handler the system calls with either the extension’s state or an error.

  - **state**: An object that describes the current state of the Safari extension, or `nil` if the system can’t find the extension.
  - **error**: An error object indicating the reason for the failure, or `nil` if no failure occurs.

## See Also

### Checking on the state of an extension
- [class func getStateOfExtension(withIdentifier: String, completionHandler: (SFSafariExtensionState?, (any Error)?) -> Void)](./getstateofextension%28withidentifier,completionhandler%29.md)
  Returns the current state of a Safari web extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/sfsafariextensionmanager/getstateofsafariextension(withidentifier:completionhandler:))*