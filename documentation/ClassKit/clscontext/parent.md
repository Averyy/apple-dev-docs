# parent

**Framework**: ClassKit  
**Kind**: property

The direct ancestor of this context.

**Availability**:
- iOS 11.4+
- iPadOS 11.4+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
weak var parent: CLSContext? { get }
```

## See Also

- [var identifierPath: [String]](clscontext/identifierpath.md)
  The identifier path that locates the context within the data store’s context hierarchy.
- [func removeFromParent()](clscontext/removefromparent.md)
  Removes the context from its parent.
- [func addChildContext(CLSContext)](clscontext/addchildcontext(_:).md)
  Adds the specifed context as a child of the context receiving the method call.
- [func descendant(matchingIdentifierPath: [String], completion: (CLSContext?, (any Error)?) -> Void)](clscontext/descendant(matchingidentifierpath:completion:).md)
  Finds the context with the given identifier path relative to this context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/classkit/clscontext/parent)*