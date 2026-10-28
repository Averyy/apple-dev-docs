# relyingPartyIdentifier

**Framework**: Authentication Services  
**Kind**: property  
**Role**: Instance Property

A string that identifies this identity’s relying party.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var relyingPartyIdentifier: String { get }
```

```objc
@property (nonatomic, copy, readonly) NSString * relyingPartyIdentifier;
```

## Discussion

A passkey credential identity reports its `relyingPartyIdentifier` value as its [`serviceIdentifier`](../ascredentialidentity/serviceidentifier.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/aspasskeycredentialidentity/relyingpartyidentifier)*