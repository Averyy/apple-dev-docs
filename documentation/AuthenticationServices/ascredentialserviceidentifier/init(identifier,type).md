# init(identifier:type:)

**Framework**: Authentication Services  
**Kind**: init  
**Role**: Initializer

Initializes a credential service identifier instance.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
init(identifier: String, type: ASCredentialServiceIdentifier.IdentifierType)
```

```objc
- (instancetype) initWithIdentifier:(NSString *) identifier type:(ASCredentialServiceIdentifierType) type;
```

## Parameters

- `identifier`: The string value for the service identifier.
- `type`: The type that the service identifier string represents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/ascredentialserviceidentifier/init(identifier:type:))*