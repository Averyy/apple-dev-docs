# CNKeyDescriptor

**Framework**: Contacts  
**Kind**: protocol  
**Role**: Protocol

This protocol is reserved for Contacts framework usage.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.11+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
protocol CNKeyDescriptor : NSCopying, NSSecureCoding, NSObjectProtocol
```

```objc
@protocol CNKeyDescriptor <NSObject, NSSecureCoding, NSCopying>
```

## Relationships

### Inherits From
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Creating a Fetch Request
- [init(keysToFetch: [any CNKeyDescriptor])](./cncontactfetchrequest/init%28keystofetch%29.md)
  Creates a fetch request for the specified keys.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cnkeydescriptor)*