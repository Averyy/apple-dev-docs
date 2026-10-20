# ODNode

**Framework**: Open Directory  
**Kind**: class  
**Role**: Class

An `ODNode` object serves as a Cocoa wrapper for an Open Directory node.

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
class ODNode
```

```objc
@interface ODNode : NSObject
```

## Topics

### Creating and Initializing a Node
- [init(session: ODSession!, name: String!) throws](./odnode/init%28session,name%29.md)
  Creates a node object with a specified session and name.
- [init(session: ODSession!, type: ODNodeType) throws](./odnode/init%28session,type%29.md)
  Creates a node object with a specified session and type.
### Querying a Node
- [func customCall(Int, send: Data!) throws -> Data](./odnode/customcall%28_,send%29.md)
  Returns the result of a custom call to the node.
- [func nodeDetails(forKeys: [Any]!) throws -> [AnyHashable : Any]](./odnode/nodedetails%28forkeys%29.md)
  Returns a dictionary containing details about a node.
- [var nodeName: String!](./odnode/nodename.md)
  The node’s name.
- [func subnodeNames() throws -> [Any]](./odnode/subnodenames%28%29.md)
  Returns the names of subnodes for the node.
- [func unreachableSubnodeNames() throws -> [Any]](./odnode/unreachablesubnodenames%28%29.md)
  Returns an array of the subnodes of a given node that are currently unreachable.
### Setting Node Credentials
- [func setCredentialsWithRecordType(String!, recordName: String!, password: String!) throws](./odnode/setcredentialswithrecordtype%28_,recordname,password%29.md)
  Sets credentials for interacting with the node.
- [func setCredentialsWithRecordType(String!, authenticationType: String!, authenticationItems: [Any]!, continueItems: AutoreleasingUnsafeMutablePointer<NSArray?>!, context: AutoreleasingUnsafeMutablePointer<AnyObject?>!) throws](./odnode/setcredentialswithrecordtype%28_,authenticationtype,authenticationitems,continueitems,context%29.md)
  Sets the credentials for interaction with the node using other types of authentication available to Open Directory.
### Managing Node Records
- [func createRecord(withRecordType: String!, name: String!, attributes: [AnyHashable : Any]!) throws -> ODRecord](./odnode/createrecord%28withrecordtype,name,attributes%29.md)
  Creates a record in a specified node with specified properties.
- [func record(withRecordType: String!, name: String!, attributes: Any!) throws -> ODRecord](./odnode/record%28withrecordtype,name,attributes%29.md)
  Returns a record from the node with a specified type and name.
- [func supportedAttributes(forRecordType: String!) throws -> [Any]](./odnode/supportedattributes%28forrecordtype%29.md)
  Returns an array of attribute types supported by the node’s records.
- [func supportedRecordTypes() throws -> [Any]](./odnode/supportedrecordtypes%28%29.md)
  Returns an array of the record types supported by the node.
### Instance Properties
- [var configuration: ODConfiguration!](./odnode/configuration.md)
### Instance Methods
- [func accountPolicies() throws -> [AnyHashable : Any]](./odnode/accountpolicies%28%29.md)
- [func addAccountPolicy([AnyHashable : Any]!, toCategory: String!) throws](./odnode/addaccountpolicy%28_,tocategory%29.md)
- [func customFunction(String!, payload: Any!) throws -> Any](./odnode/customfunction%28_,payload%29.md)
- [func passwordContentCheck(String!, forRecordName: String!) throws](./odnode/passwordcontentcheck%28_,forrecordname%29.md)
- [func policies() throws -> [AnyHashable : Any]](./odnode/policies%28%29.md)
- [func removeAccountPolicy([AnyHashable : Any]!, fromCategory: String!) throws](./odnode/removeaccountpolicy%28_,fromcategory%29.md)
- [func removePolicy(String!) throws](./odnode/removepolicy%28_%29.md)
- [func setAccountPolicies([AnyHashable : Any]!) throws](./odnode/setaccountpolicies%28_%29.md)
- [func setPolicies([AnyHashable : Any]!) throws](./odnode/setpolicies%28_%29.md)
- [func setPolicy(String!, value: Any!) throws](./odnode/setpolicy%28_,value%29.md)
- [func supportedPolicies() throws -> [AnyHashable : Any]](./odnode/supportedpolicies%28%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Classes
- [class ODAttributeMap](./odattributemap.md)
- [class ODConfiguration](./odconfiguration.md)
- [class ODContext](./odcontext.md)
  An Open Directory context type.
- [class ODMappings](./odmappings.md)
- [class ODModuleEntry](./odmoduleentry.md)
- [class ODNodeRef](./odnoderef.md)
  An Open Directory node type.
- [class ODQuery](./odquery.md)
  An `ODQuery` object serves as a Cocoa wrapper for an Open Directory query.
- [class ODQueryRef](./odqueryref.md)
  An Open Directory query type.
- [class ODRecord](./odrecord.md)
  An `ODRecord` object serves as a Cocoa wrapper for an Open Directory record.
- [class ODRecordMap](./odrecordmap.md)
- [class ODRecordRef](./odrecordref.md)
  An Open Directory record type.
- [class ODSession](./odsession.md)
  An `ODSession` object serves as a Cocoa wrapper for an Open Directory session.
- [class ODSessionRef](./odsessionref.md)
  An Open Directory session type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/opendirectory/odnode)*