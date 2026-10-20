# openCredentialProviderAppSettings(completionHandler:)

**Framework**: Authentication Services  
**Kind**: method  
**Role**: Type Method

Open the Settings app and navigate to the AutoFill provider settings.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class func openCredentialProviderAppSettings(completionHandler: (@Sendable ((any Error)?) -> Void)? = nil)
```

```swift
class func openCredentialProviderAppSettings() async throws
```

```objc
+ (void) openCredentialProviderAppSettingsWithCompletionHandler:(void (^)(NSError *error)) completionHandler;
```

## Parameters

- `completionHandler`: An optional block that the system calls on completion.

## See Also

### Opening the Settings app
- [class func openVerificationCodeAppSettings(completionHandler: (((any Error)?) -> Void)?)](./openverificationcodeappsettings%28completionhandler%29.md)
  Open the Settings app and navigate to the verification code provider settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/assettingshelper/opencredentialproviderappsettings(completionhandler:))*