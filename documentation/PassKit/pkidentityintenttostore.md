# PKIdentityIntentToStore

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: class

An object that represents your intention to store an identity element or values derived from an identity element.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
class PKIdentityIntentToStore
```

## Topics

### Creating a default intent
- [class func mayStore(days: Int) -> Self](pkidentityintenttostore/maystore(days:).md)
  An object that indicates your app may store a data element for the length of time you specify.
### Getting default intents
- [class var mayStore: PKIdentityIntentToStore](pkidentityintenttostore/maystore.md)
  An object that indicates your app may store a data element for an indefinite length of time.
- [class var willNotStore: PKIdentityIntentToStore](pkidentityintenttostore/willnotstore.md)
  An object that indicates your app won’t store a data element any longer than necessary to complete a request.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class PKIdentityDriversLicenseDescriptor](pkidentitydriverslicensedescriptor.md)
  An object for requesting information from a user’s driver’s license or equivalent document.
- [protocol PKIdentityDocumentDescriptor](pkidentitydocumentdescriptor.md)
  A type that describes the structure and behavior of an identity document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkidentityintenttostore)*