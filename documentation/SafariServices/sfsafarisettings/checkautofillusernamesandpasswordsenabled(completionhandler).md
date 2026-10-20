# checkAutoFillUserNamesAndPasswordsEnabled(completionHandler:)

**Framework**: Safari Services  
**Kind**: method  
**Role**: Type Method

Query the value of the Safari settings toggle for AutoFill > User names and passwords

**Availability**:
- Mac Catalyst 27.0+
- macOS 27.0+

## Declaration

```swift
class func checkAutoFillUserNamesAndPasswordsEnabled(completionHandler: @escaping @Sendable (Bool, (any Error)?) -> Void)
```

```swift
class var isAutoFillUserNamesAndPasswordsEnabled: Bool { get async throws }
```

```objc
+ (void) checkAutoFillUserNamesAndPasswordsEnabledWithCompletionHandler:(void (^)(BOOL isEnabled, NSError *error)) completionHandler;
```

## Parameters

- `completionHandler`: The block the system calls after the operation complets, with a boolean parameter representing the toggle value.

  - **isEnabled**: A boolean value representing the current value of the toggle.
  - **error**: An SFSafariSettingsError if any occurred. If non-nil, the value of `isEnabled`


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/sfsafarisettings/checkautofillusernamesandpasswordsenabled(completionhandler:))*