# ODQuery

**Framework**: Open Directory  
**Kind**: class  
**Role**: Class

An `ODQuery` object serves as a Cocoa wrapper for an Open Directory query.

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
class ODQuery
```

```objc
@interface ODQuery : NSObject
```

## Topics

### Creating and Initializing a Query
- [init(node: ODNode!, forRecordTypes: Any!, attribute: String!, matchType: ODMatchType, queryValues: Any!, returnAttributes: Any!, maximumResults: Int) throws](./odquery/init%28node,forrecordtypes,attribute,matchtype,queryvalues,returnattributes,maximumresults%29.md)
  Creates a query object with provided parameters.
### Managing Asynchronous Queries
- [var delegate: (any ODQueryDelegate)!](./odquery/delegate.md)
  The query’s delegate.
- [var operationQueue: OperationQueue!](./odquery/operationqueue.md)
  The queue on which asynchronous results are delivered to the delegate.
- [func schedule(in: RunLoop!, forMode: String!)](./odquery/schedule%28in,formode%29.md)
  Retrieves results from a query asynchronously by scheduling the query in a run loop.
- [func remove(from: RunLoop!, forMode: String!)](./odquery/remove%28from,formode%29.md)
  Removes the query from a specified run loop.
- [func synchronize()](./odquery/synchronize%28%29.md)
  Restarts a query, disposing of any results it has obtained.
### Managing Synchronous Queries
- [func resultsAllowingPartial(Bool) throws -> [Any]](./odquery/resultsallowingpartial%28_%29.md)
  Returns results from a query synchronously.

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

*[View on Apple Developer](https://developer.apple.com/documentation/opendirectory/odquery)*