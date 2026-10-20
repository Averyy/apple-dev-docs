# recordIdentifier

**Framework**: Authentication Services  
**Kind**: property  
**Role**: Instance Property

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
- [var credentialID: Data](./credentialid.md)
  The credential identifier for this passkey credential identity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/aspasskeycredentialidentity/recordidentifier)*