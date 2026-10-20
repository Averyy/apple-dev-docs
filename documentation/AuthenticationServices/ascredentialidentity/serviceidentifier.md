# serviceIdentifier

**Framework**: Authentication Services  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

An identifier that helps the system know with which apps or websites to associate this credential.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var serviceIdentifier: ASCredentialServiceIdentifier { get }
```

```objc
@property (nonatomic, strong, readonly) ASCredentialServiceIdentifier * serviceIdentifier;
```

## See Also

### Distinguishing identities
- [var recordIdentifier: String?](./recordidentifier.md)
  A string used to correlate this identity to a record in your app’s own database.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/ascredentialidentity/serviceidentifier)*