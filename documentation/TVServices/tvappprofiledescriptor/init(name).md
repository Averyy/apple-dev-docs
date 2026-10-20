# init(name:)

**Framework**: TV Services  
**Kind**: init  
**Role**: Initializer

Creates a new app profile descriptor object with the specified name.

**Availability**:
- tvOS 13.0+ - Deprecated in 16.0

> **Deprecated**: User Management capability get-current-user is no longer supported. Please use runs-as-current-user-with-user-independent-keychain and kSecUseUserIndependentKeychain for sharing keychain items across users.

## Declaration

```swift
init(name: String)
```

```objc
- (instancetype) initWithName:(NSString *) name;
```

#### Return Value

An initialized app profile descriptor object.

## Parameters

- `name`: The user-visible string to display for the profile.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvservices/tvappprofiledescriptor/init(name:))*