# ODNode

**Framework**: Open Directory  
**Kind**: class

An `ODNode` object serves as a Cocoa wrapper for an Open Directory node.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
class ODNode
```

## Topics

### Creating and Initializing a Node
- [init(session: ODSession!, name: String!) throws](odnode/init(session:name:).md)
  Creates a node object with a specified session and name.
- [init(session: ODSession!, type: ODNodeType) throws](odnode/init(session:type:).md)
  Creates a node object with a specified session and type.
### Querying a Node
- [func customCall(Int, send: Data!) throws -> Data](odnode/customcall(_:send:).md)
  Returns the result of a custom call to the node.
- [func nodeDetails(forKeys: [Any]!) throws -> [AnyHashable : Any]](odnode/nodedetails(forkeys:).md)
  Returns a dictionary containing details about a node.
- [var nodeName: String!](odnode/nodename.md)
  The node’s name.
- [func subnodeNames() throws -> [Any]](odnode/subnodenames.md)
  Returns the names of subnodes for the node.
- [func unreachableSubnodeNames() throws -> [Any]](odnode/unreachablesubnodenames.md)
  Returns an array of the subnodes of a given node that are currently unreachable.
### Setting Node Credentials
- [func setCredentialsWithRecordType(String!, recordName: String!, password: String!) throws](odnode/setcredentialswithrecordtype(_:recordname:password:).md)
  Sets credentials for interacting with the node.
- [func setCredentialsWithRecordType(String!, authenticationType: String!, authenticationItems: [Any]!, continueItems: AutoreleasingUnsafeMutablePointer<NSArray?>!, context: AutoreleasingUnsafeMutablePointer<AnyObject?>!) throws](odnode/setcredentialswithrecordtype(_:authenticationtype:authenticationitems:continueitems:context:).md)
  Sets the credentials for interaction with the node using other types of authentication available to Open Directory.
### Managing Node Records
- [func createRecord(withRecordType: String!, name: String!, attributes: [AnyHashable : Any]!) throws -> ODRecord](odnode/createrecord(withrecordtype:name:attributes:).md)
  Creates a record in a specified node with specified properties.
- [func record(withRecordType: String!, name: String!, attributes: Any!) throws -> ODRecord](odnode/record(withrecordtype:name:attributes:).md)
  Returns a record from the node with a specified type and name.
- [func supportedAttributes(forRecordType: String!) throws -> [Any]](odnode/supportedattributes(forrecordtype:).md)
  Returns an array of attribute types supported by the node’s records.
- [func supportedRecordTypes() throws -> [Any]](odnode/supportedrecordtypes.md)
  Returns an array of the record types supported by the node.
### Instance Properties
- [var configuration: ODConfiguration!](odnode/configuration.md)
### Instance Methods
- [func accountPolicies() throws -> [AnyHashable : Any]](odnode/accountpolicies.md)
- [func addAccountPolicy([AnyHashable : Any]!, toCategory: String!) throws](odnode/addaccountpolicy(_:tocategory:).md)
- [func customFunction(String!, payload: Any!) throws -> Any](odnode/customfunction(_:payload:).md)
- [func passwordContentCheck(String!, forRecordName: String!) throws](odnode/passwordcontentcheck(_:forrecordname:).md)
- [func policies() throws -> [AnyHashable : Any]](odnode/policies.md)
- [func removeAccountPolicy([AnyHashable : Any]!, fromCategory: String!) throws](odnode/removeaccountpolicy(_:fromcategory:).md)
- [func removePolicy(String!) throws](odnode/removepolicy(_:).md)
- [func setAccountPolicies([AnyHashable : Any]!) throws](odnode/setaccountpolicies(_:).md)
- [func setPolicies([AnyHashable : Any]!) throws](odnode/setpolicies(_:).md)
- [func setPolicy(String!, value: Any!) throws](odnode/setpolicy(_:value:).md)
- [func supportedPolicies() throws -> [AnyHashable : Any]](odnode/supportedpolicies.md)

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
- [class ODConfiguration](odconfiguration.md)
- [class ODContext](odcontext.md)
  An Open Directory context type.
- [class ODMappings](odmappings.md)
- [class ODModuleEntry](odmoduleentry.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/opendirectory/odnode)*