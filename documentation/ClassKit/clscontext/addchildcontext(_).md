# addChildContext(_:)

**Framework**: ClassKit  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) addChildContext:(CLSContext *) child;
```

## Discussion

You don’t need to call this method directly. Instead, use the [`CLSDataStoreDelegate`](../clsdatastoredelegate.md) protocol to build contexts.

## Parameters

- `child`: The context to add as a child of the one receiving the method call.

## See Also

### Managing context hierarchy
- [var identifierPath: [String]](./identifierpath.md)
  The identifier path that locates the context within the data store’s context hierarchy.
- [var parent: CLSContext?](./parent.md)
  The direct ancestor of this context.
- [func removeFromParent()](./removefromparent%28%29.md)
  Removes the context from its parent.
- [func descendant(matchingIdentifierPath: [String], completion: (CLSContext?, (any Error)?) -> Void)](./descendant%28matchingidentifierpath,completion%29.md)
  Finds the context with the given identifier path relative to this context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/classkit/clscontext/addchildcontext(_:))*