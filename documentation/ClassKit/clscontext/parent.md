# parent

**Framework**: ClassKit  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, weak, readonly, nullable) CLSContext * parent;
```

## See Also

### Managing context hierarchy
- [var identifierPath: [String]](./identifierpath.md)
  The identifier path that locates the context within the data store’s context hierarchy.
- [func removeFromParent()](./removefromparent%28%29.md)
  Removes the context from its parent.
- [func addChildContext(CLSContext)](./addchildcontext%28_%29.md)
  Adds the specifed context as a child of the context receiving the method call.
- [func descendant(matchingIdentifierPath: [String], completion: (CLSContext?, (any Error)?) -> Void)](./descendant%28matchingidentifierpath,completion%29.md)
  Finds the context with the given identifier path relative to this context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/classkit/clscontext/parent)*