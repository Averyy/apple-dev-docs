# ODSessionRef

**Framework**: Open Directory  
**Kind**: class  
**Role**: Class

An Open Directory session type.

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
class ODSessionRef
```

```c
typedef struct __ODSession * ODSessionRef;
```

#### Discussion

Session objects are usually created with [`ODSessionCreate(_:_:_:)`](./odsessioncreate%28_,_,_%29.md), and are typically passed to node functions.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)

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
- [class ODSession](./odsession.md)
  An `ODSession` object serves as a Cocoa wrapper for an Open Directory session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/opendirectory/odsessionref)*