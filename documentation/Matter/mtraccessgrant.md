# MTRAccessGrant

**Framework**: Matter  
**Kind**: class  
**Role**: Class

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

```objc
@interface MTRAccessGrant : NSObject
```

## Topics

### Initializers
- [init(forAllNodesWith: MTRAccessControlEntryPrivilege)](./mtraccessgrant/init%28forallnodeswith%29.md)
- [init?(forCASEAuthenticatedTag: NSNumber, privilege: MTRAccessControlEntryPrivilege)](./mtraccessgrant/init%28forcaseauthenticatedtag,privilege%29.md)
- [init?(forGroupID: NSNumber, privilege: MTRAccessControlEntryPrivilege)](./mtraccessgrant/init%28forgroupid,privilege%29.md)
- [init?(forNodeID: NSNumber, privilege: MTRAccessControlEntryPrivilege)](./mtraccessgrant/init%28fornodeid,privilege%29.md)
- [init(forAllNodesWithPrivilege: MTRAccessControlEntryPrivilege)](./mtraccessgrant/init%28forallnodeswithprivilege%29.md)
### Instance Properties
- [var authenticationMode: MTRAccessControlEntryAuthMode](./mtraccessgrant/authenticationmode.md)
- [var grantedPrivilege: MTRAccessControlEntryPrivilege](./mtraccessgrant/grantedprivilege.md)
- [var subjectID: NSNumber?](./mtraccessgrant/subjectid.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtraccessgrant)*