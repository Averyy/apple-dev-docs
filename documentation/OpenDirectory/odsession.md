# ODSession

**Framework**: Open Directory  
**Kind**: class  
**Role**: Class

An `ODSession` object serves as a Cocoa wrapper for an Open Directory session.

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
class ODSession
```

```objc
@interface ODSession : NSObject
```

## Topics

### Creating and Accessing Sessions
- [class func `default`() -> ODSession!](./odsession/default%28%29.md)
  Returns a shared instance of the local session.
- [init(options: [AnyHashable : Any]!) throws](./odsession/init%28options%29.md)
  Creates a session object directed over proxy to another host.
### Accessing Node Information
- [func nodeNames() throws -> [Any]](./odsession/nodenames%28%29.md)
  Returns the node names that are registered with this session.
### Constants
- [ODSession Option Keys](./odsession-option-keys.md)
  Option keys used when creating a session directed over a proxy.
### Instance Properties
- [var configurationTemplateNames: [Any]!](./odsession/configurationtemplatenames.md)
- [var mappingTemplateNames: [Any]!](./odsession/mappingtemplatenames.md)
### Instance Methods
- [func add(ODConfiguration!, authorization: SFAuthorization!) throws](./odsession/add%28_,authorization%29.md)
- [func configuration(forNodename: String!) -> ODConfiguration!](./odsession/configuration%28fornodename%29.md)
- [func configurationAuthorizationAllowingUserInteraction(Bool) throws -> SFAuthorization](./odsession/configurationauthorizationallowinguserinteraction%28_%29.md)
- [func delete(ODConfiguration!, authorization: SFAuthorization!) throws](./odsession/delete%28_,authorization%29.md)
- [func deleteConfiguration(withNodename: String!, authorization: SFAuthorization!) throws](./odsession/deleteconfiguration%28withnodename,authorization%29.md)

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
- [class ODNode](./odnode.md)
  An `ODNode` object serves as a Cocoa wrapper for an Open Directory node.
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
- [class ODSessionRef](./odsessionref.md)
  An Open Directory session type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/opendirectory/odsession)*