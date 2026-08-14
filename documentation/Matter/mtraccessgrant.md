# MTRAccessGrant

**Framework**: Matter  
**Kind**: class

**Availability**:
- iOS 17.6+
- iPadOS 17.6+
- Mac Catalyst 17.6+
- macOS 14.6+
- tvOS 17.6+
- visionOS 1.0+
- watchOS 10.6+

## Declaration

```swift
class MTRAccessGrant
```

## Topics

### Initializers
- [init(forAllNodesWith: MTRAccessControlEntryPrivilege)](mtraccessgrant/init(forallnodeswith:).md)
- [init?(forCASEAuthenticatedTag: NSNumber, privilege: MTRAccessControlEntryPrivilege)](mtraccessgrant/init(forcaseauthenticatedtag:privilege:).md)
- [init?(forGroupID: NSNumber, privilege: MTRAccessControlEntryPrivilege)](mtraccessgrant/init(forgroupid:privilege:).md)
- [init?(forNodeID: NSNumber, privilege: MTRAccessControlEntryPrivilege)](mtraccessgrant/init(fornodeid:privilege:).md)
- [init(forAllNodesWithPrivilege: MTRAccessControlEntryPrivilege)](mtraccessgrant/init(forallnodeswithprivilege:).md)
### Instance Properties
- [var authenticationMode: MTRAccessControlEntryAuthMode](mtraccessgrant/authenticationmode.md)
- [var grantedPrivilege: MTRAccessControlEntryPrivilege](mtraccessgrant/grantedprivilege.md)
- [var subjectID: NSNumber?](mtraccessgrant/subjectid.md)

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtraccessgrant)*