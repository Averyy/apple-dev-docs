# init(object:type:index:)

**Framework**: Foundation  
**Kind**: init

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

## Parameters

- `anObject`: An optional object the change will remove or insert.
- `type`: The type of change.
- `index`: The index location within an ordered collection where the change applies.

## See Also

- [init(object: Any?, type: NSCollectionChangeType, index: Int, associatedIndex: Int)](nsorderedcollectionchange/init(object:type:index:associatedindex:).md)
  Creates a change object that represents inserting, removing, or moving an object from an ordered collection at a specific index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsorderedcollectionchange/init(object:type:index:))*