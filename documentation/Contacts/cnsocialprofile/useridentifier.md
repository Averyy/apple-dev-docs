# userIdentifier

**Framework**: Contacts  
**Kind**: property  
**Role**: Instance Property

The service’s user identifier associated with the social profile.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var userIdentifier: String { get }
```

*iOS, iPadOS, Mac Catalyst, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly) NSString * userIdentifier;
```

*macOS*

```objc
@property (atomic, copy, readonly) NSString * userIdentifier;
```

## See Also

### Getting Social Profile Information
- [var username: String](./username.md)
  The user name for the social profile.
- [var service: String](./service.md)
  The social profile’s service name.
- [var urlString: String](./urlstring.md)
  The URL associated with the social profile.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cnsocialprofile/useridentifier)*