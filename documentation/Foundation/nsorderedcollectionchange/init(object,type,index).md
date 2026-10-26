# init(object:type:index:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Creates a change object that represents inserting or removing an object from an ordered collection at a specific index.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
convenience init(object anObject: Any?, type: NSCollectionChangeType, index: Int)
```

```objc
- (instancetype) initWithObject:(ObjectType) anObject type:(NSCollectionChangeType) type index:(NSUInteger) index;
```

## Parameters

- `anObject`: An optional object the change will remove or insert.
- `type`: The type of change.
- `index`: The index location within an ordered collection where the change applies.

## See Also

### Creating a Change
- [init(object: Any?, type: NSCollectionChangeType, index: Int, associatedIndex: Int)](./init%28object,type,index,associatedindex%29.md)
  Creates a change object that represents inserting, removing, or moving an object from an ordered collection at a specific index.
- [+ changeWithObject:type:index:](./changewithobject_type_index_.md)
  Creates an change object that represents inserting or removing an object from an ordered collection at a specific index.
- [+ changeWithObject:type:index:associatedIndex:](./changewithobject_type_index_associatedindex_.md)
  Creates an change object that represents inserting or removing an object from an ordered collection at a specific index, matched with an associated location that infers a move within the collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsorderedcollectionchange/init(object:type:index:))*