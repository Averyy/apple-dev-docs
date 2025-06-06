# removeFromParent()

**Framework**: ClassKit  
**Kind**: method

Removes the context from its parent.

**Availability**:
- iOS 11.4+
- iPadOS 11.4+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func removeFromParent()
```

#### Discussion

If you remove a context from its parent and don’t add it as the child of another context before you call [`save(completion:)`](clsdatastore/save(completion:).md), then the framework deletes the context entirely.

## See Also

- [var identifierPath: [String]](clscontext/identifierpath.md)
  The identifier path that locates the context within the data store’s context hierarchy.
- [var parent: CLSContext?](clscontext/parent.md)
  The direct ancestor of this context.
- [func addChildContext(CLSContext)](clscontext/addchildcontext(_:).md)
  Adds the specifed context as a child of the context receiving the method call.
- [func descendant(matchingIdentifierPath: [String], completion: (CLSContext?, (any Error)?) -> Void)](clscontext/descendant(matchingidentifierpath:completion:).md)
  Finds the context with the given identifier path relative to this context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/classkit/clscontext/removefromparent())*