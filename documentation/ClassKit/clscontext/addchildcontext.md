# addChildContext(_:)

**Framework**: ClassKit  
**Kind**: method

Adds the specifed context as a child of the context receiving the method call.

**Availability**:
- iOS 11.4+
- iPadOS 11.4+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func addChildContext(_ child: CLSContext)
```

#### Discussion

Typically you use the [`CLSDataStoreDelegate`](clsdatastoredelegate.md) protocol to build contexts, in which case you don’t need to call this method directly.

## Parameters

- `child`: The context to add as a child of the one receiving the method call.

## See Also

- [var identifierPath: [String]](clscontext/identifierpath.md)
  The identifier path that locates the context within the data store’s context hierarchy.
- [var parent: CLSContext?](clscontext/parent.md)
  The direct ancestor of this context.
- [func removeFromParent()](clscontext/removefromparent.md)
  Removes the context from its parent.
- [func descendant(matchingIdentifierPath: [String], completion: (CLSContext?, (any Error)?) -> Void)](clscontext/descendant(matchingidentifierpath:completion:).md)
  Finds the context with the given identifier path relative to this context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/classkit/clscontext/addchildcontext(_:))*