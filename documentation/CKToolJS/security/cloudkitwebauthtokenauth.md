# CloudKitWebAuthTokenAuth

**Framework**: CKTool JS  
**Kind**: property

Your CloudKit Web Authentication token.

**Availability**:
- CKTool JS 1.2.15+

## Declaration

```swift
attribute string? CloudKitWebAuthTokenAuth;
```

#### Discussion

If you are accessing user data using a CloudKit Web Authentication token, you set this to the token value.

Note: You must also set `CloudKitAPITokenAuth` if you set this value.

For more information on accessing CloudKit using a Web Authentication token, see https://developer.apple.com/library/archive/documentation/DataManagement/Conceptual/CloudKitWebServicesReference/SettingUpWebServices.html#//apple_ref/doc/uid/TP40015240-CH24-SW1


---

*[View on Apple Developer](https://developer.apple.com/documentation/cktooljs/security/cloudkitwebauthtokenauth)*