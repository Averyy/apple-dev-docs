# removeFromParent()

**Framework**: ClassKit  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) removeFromParent;
```

## Discussion

If you remove a context from its parent and don’t add it as the child of another context before you call [`save(completion:)`](../clsdatastore/save%28completion%29.md), then the framework deletes the context entirely.

## See Also

### Managing context hierarchy
- [var identifierPath: [String]](./identifierpath.md)
  The identifier path that locates the context within the data store’s context hierarchy.
- [var parent: CLSContext?](./parent.md)
  The direct ancestor of this context.
- [func addChildContext(CLSContext)](./addchildcontext%28_%29.md)
  Adds the specifed context as a child of the context receiving the method call.
- [func descendant(matchingIdentifierPath: [String], completion: (CLSContext?, (any Error)?) -> Void)](./descendant%28matchingidentifierpath,completion%29.md)
  Finds the context with the given identifier path relative to this context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/classkit/clscontext/removefromparent())*