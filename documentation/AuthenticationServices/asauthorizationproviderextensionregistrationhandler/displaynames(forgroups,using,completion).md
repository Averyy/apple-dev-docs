# displayNames(forGroups:using:completion:)

**Framework**: Authentication Services  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- macOS 26.0+

## Declaration

```swift
optional func displayNames(forGroups groups: [String], using loginManager: ASAuthorizationProviderExtensionLoginManager, completion: @escaping @Sendable ([String : String]) -> Void)
```

```swift
optional func displayNames(forGroups groups: [String], using loginManager: ASAuthorizationProviderExtensionLoginManager) async -> [String : String]
```

```objc
- (void) displayNamesForGroups:(NSArray<NSString *> *) groups loginManager:(ASAuthorizationProviderExtensionLoginManager *) loginManager completion:(void (^)(NSDictionary<NSString *,NSString *> *fullNames)) completion;
```

#### Discussion

Request the display names for the supplied group identifiers.  The completion key is the identifier and the value is the display name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationproviderextensionregistrationhandler/displaynames(forgroups:using:completion:))*