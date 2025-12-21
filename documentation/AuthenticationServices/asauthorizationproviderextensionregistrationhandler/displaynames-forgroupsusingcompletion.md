# displayNames(forGroups:using:completion:)

**Framework**: Authentication Services  
**Kind**: method

**Availability**:
- macOS 26.0+

## Declaration

```swift
optional func displayNames(forGroups groups: [String], using loginManager: ASAuthorizationProviderExtensionLoginManager) async -> [String : String]
```

#### Discussion

Request the display names for the supplied group identifiers.  The completion key is the identifier and the value is the display name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationproviderextensionregistrationhandler/displaynames(forgroups:using:completion:))*