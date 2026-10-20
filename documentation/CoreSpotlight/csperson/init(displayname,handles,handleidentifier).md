# init(displayName:handles:handleIdentifier:)

**Framework**: Core Spotlight  
**Kind**: init  
**Role**: Initializer

Returns a new `CSPerson` object initialized with the specified display name and contact attributes.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
init(displayName: String?, handles: [String], handleIdentifier: String)
```

```objc
- (instancetype) initWithDisplayName:(NSString *) displayName handles:(NSArray<NSString *> *) handles handleIdentifier:(NSString *) handleIdentifier;
```

#### Return Value

An initialized person object that represents a user’s contact.

## Parameters

- `displayName`: The name of the person in a user-displayable string.
- `handles`: An array of contact handles, such as phone number or email address.
- `handleIdentifier`: A property key that specifies a handle type, such as [`CNContactEmailAddressesKey`](../../Contacts/cncontactemailaddresseskey.md).

## See Also

### Initializing a person object
- [init?(coder: NSCoder)](./init%28coder%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/csperson/init(displayname:handles:handleidentifier:))*