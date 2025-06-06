# ASSettingsHelper

**Framework**: Authentication Services  
**Kind**: class

A class that opens Settings and navigates to the settings for configuring credential providers.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class ASSettingsHelper
```

## Topics

### Opening the Settings app
- [class func openCredentialProviderAppSettings(completionHandler: (((any Error)?) -> Void)?)](assettingshelper/opencredentialproviderappsettings(completionhandler:).md)
  Open the Settings app and navigate to the AutoFill provider settings.
- [class func openVerificationCodeAppSettings(completionHandler: (((any Error)?) -> Void)?)](assettingshelper/openverificationcodeappsettings(completionhandler:).md)
  Open the Settings app and navigate to the verification code provider settings.
### Type Methods
- [class func requestToTurnOnCredentialProviderExtension(completionHandler: (Bool) -> Void)](assettingshelper/requesttoturnoncredentialproviderextension(completionhandler:).md)
  Call this method from your containing app to request to turn on a contained Credential Provider Extension. If the extension is not currently enabled, a prompt will be shown to allow it to be turned on. The completion handler is called with YES or NO depending on whether the credential provider is enabled. You need to wait 10 seconds in order to make additional request to this API.

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/assettingshelper)*