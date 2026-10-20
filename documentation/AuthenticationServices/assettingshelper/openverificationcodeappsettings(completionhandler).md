# openVerificationCodeAppSettings(completionHandler:)

**Framework**: Authentication Services  
**Kind**: method  
**Role**: Type Method

Open the Settings app and navigate to the verification code provider settings.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class func openVerificationCodeAppSettings(completionHandler: (@Sendable ((any Error)?) -> Void)? = nil)
```

```swift
class func openVerificationCodeAppSettings() async throws
```

```objc
+ (void) openVerificationCodeAppSettingsWithCompletionHandler:(void (^)(NSError *error)) completionHandler;
```

## Parameters

- `completionHandler`: An optional block that the system calls on completion.

## See Also

### Opening the Settings app
- [class func openCredentialProviderAppSettings(completionHandler: (((any Error)?) -> Void)?)](./opencredentialproviderappsettings%28completionhandler%29.md)
  Open the Settings app and navigate to the AutoFill provider settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/assettingshelper/openverificationcodeappsettings(completionhandler:))*