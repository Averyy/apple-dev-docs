# ODConfiguration

**Framework**: Open Directory  
**Kind**: class

**Availability**:
- Mac Catalyst ?+
- macOS 10.9+

## Declaration

```swift
class ODConfiguration
```

## Topics

### Instance Properties
- [var authenticationModuleEntries: [Any]!](odconfiguration/authenticationmoduleentries-swift.property.md)
- [var comment: String!](odconfiguration/comment-swift.property.md)
- [var connectionIdleTimeoutInSeconds: Int](odconfiguration/connectionidletimeoutinseconds-swift.property.md)
- [var connectionSetupTimeoutInSeconds: Int](odconfiguration/connectionsetuptimeoutinseconds-swift.property.md)
- [var defaultMappings: ODMappings!](odconfiguration/defaultmappings-swift.property.md)
- [var defaultModuleEntries: [Any]!](odconfiguration/defaultmoduleentries-swift.property.md)
- [var discoveryModuleEntries: [Any]!](odconfiguration/discoverymoduleentries-swift.property.md)
- [var generalModuleEntries: [Any]!](odconfiguration/generalmoduleentries-swift.property.md)
- [var hideRegistration: Bool](odconfiguration/hideregistration-swift.property.md)
- [var manInTheMiddleProtection: Bool](odconfiguration/maninthemiddleprotection-swift.property.md)
- [var nodeName: String!](odconfiguration/nodename-swift.property.md)
- [var packetEncryption: Int](odconfiguration/packetencryption-swift.property.md)
- [var packetSigning: Int](odconfiguration/packetsigning-swift.property.md)
- [var preferredDestinationHostName: String!](odconfiguration/preferreddestinationhostname-swift.property.md)
- [var preferredDestinationHostPort: UInt16](odconfiguration/preferreddestinationhostport-swift.property.md)
- [var queryTimeoutInSeconds: Int](odconfiguration/querytimeoutinseconds-swift.property.md)
- [var templateName: String!](odconfiguration/templatename-swift.property.md)
- [var trustAccount: String!](odconfiguration/trustaccount-swift.property.md)
- [var trustKerberosPrincipal: String!](odconfiguration/trustkerberosprincipal-swift.property.md)
- [var trustMetaAccount: String!](odconfiguration/trustmetaaccount-swift.property.md)
- [var trustType: String!](odconfiguration/trusttype-swift.property.md)
- [var trustUsesKerberosKeytab: Bool](odconfiguration/trustuseskerberoskeytab-swift.property.md)
- [var trustUsesMutualAuthentication: Bool](odconfiguration/trustusesmutualauthentication-swift.property.md)
- [var trustUsesSystemKeychain: Bool](odconfiguration/trustusessystemkeychain-swift.property.md)
- [var virtualSubnodes: [Any]!](odconfiguration/virtualsubnodes-swift.property.md)
### Instance Methods
- [func addTrustType(String!, trustAccount: String!, trustPassword: String!, username: String!, password: String!, joinExisting: Bool) throws](odconfiguration/addtrusttype(_:trustaccount:trustpassword:username:password:joinexisting:).md)
- [func removeTrust(usingUsername: String!, password: String!, deleteTrustAccount: Bool) throws](odconfiguration/removetrust(usingusername:password:deletetrustaccount:).md)
- [func save(using: SFAuthorization!) throws](odconfiguration/save(using:).md)
### Type Methods
- [class func suggestedTrustAccount(String!) -> String!](odconfiguration/suggestedtrustaccount(_:).md)
- [class func suggestedTrustPassword(Int) -> String!](odconfiguration/suggestedtrustpassword(_:).md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class ODAttributeMap](odattributemap.md)
- [class ODContext](odcontext.md)
  An Open Directory context type.
- [class ODMappings](odmappings.md)
- [class ODModuleEntry](odmoduleentry.md)
- [class ODNode](odnode.md)
  An `ODNode` object serves as a Cocoa wrapper for an Open Directory node.
- [class ODNodeRef](odnoderef.md)
  An Open Directory node type.
- [class ODQuery](odquery.md)
  An `ODQuery` object serves as a Cocoa wrapper for an Open Directory query.
- [class ODQueryRef](odqueryref.md)
  An Open Directory query type.
- [class ODRecord](odrecord.md)
  An `ODRecord` object serves as a Cocoa wrapper for an Open Directory record.
- [class ODRecordMap](odrecordmap.md)
- [class ODRecordRef](odrecordref.md)
  An Open Directory record type.
- [class ODSession](odsession.md)
  An `ODSession` object serves as a Cocoa wrapper for an Open Directory session.
- [class ODSessionRef](odsessionref.md)
  An Open Directory session type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/opendirectory/odconfiguration)*