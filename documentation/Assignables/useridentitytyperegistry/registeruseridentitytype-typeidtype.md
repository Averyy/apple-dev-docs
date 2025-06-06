# registerUserIdentityType(typeID:type:)

**Framework**: Assignables  
**Kind**: method

Registers a user identity type for use when deserializing the user identity from `Data`.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- visionOS ?+

## Declaration

```swift
static func registerUserIdentityType<UI>(typeID: String, type: UI.Type) where UI : UserIdentity
```

## Parameters

- `typeID`: A unique type identifier for the user identity to register
- `type`: The type of the user identity to register.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/useridentitytyperegistry/registeruseridentitytype(typeid:type:))*