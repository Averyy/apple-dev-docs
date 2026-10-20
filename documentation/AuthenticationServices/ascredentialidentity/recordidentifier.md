# recordIdentifier

**Framework**: Authentication Services  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

A string used to correlate this identity to a record in your app’s own database.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var recordIdentifier: String? { get }
```

```objc
@property (nonatomic, copy, readonly, nullable) NSString * recordIdentifier;
```

## See Also

### Distinguishing identities
- [var serviceIdentifier: ASCredentialServiceIdentifier](./serviceidentifier.md)
  An identifier that helps the system know with which apps or websites to associate this credential.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/ascredentialidentity/recordidentifier)*