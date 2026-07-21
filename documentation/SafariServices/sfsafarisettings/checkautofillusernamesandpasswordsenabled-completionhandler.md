# checkAutoFillUserNamesAndPasswordsEnabled(completionHandler:)

**Framework**: Safari Services  
**Kind**: method

Query the value of the Safari settings toggle for AutoFill > User names and passwords

**Availability**:
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)

## Declaration

```swift
class var isAutoFillUserNamesAndPasswordsEnabled: Bool { get async throws }
```

## Parameters

- `completionHandler`: The block the system calls after the operation complets, with a boolean parameter representing the toggle value. - **isEnabled**: A boolean value representing the current value of the toggle.
- **error**: An SFSafariSettingsError if any occurred. If non-nil, the value of `isEnabled`


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/sfsafarisettings/checkautofillusernamesandpasswordsenabled(completionhandler:))*