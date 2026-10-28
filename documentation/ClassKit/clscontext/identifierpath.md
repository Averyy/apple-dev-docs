# identifierPath

**Framework**: ClassKit  
**Kind**: property  
**Role**: Instance Property

The identifier path that locates the context within the data store’s context hierarchy.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var identifierPath: [String] { get }
```

```objc
@property (nonatomic, copy, readonly) NSArray<NSString *> * identifierPath;
```

## Discussion

You can use the value stored in this property when calling the [`contexts(matchingIdentifierPath:completion:)`](../clsdatastore/contexts%28matchingidentifierpath,completion%29.md) method to retrieve the current context.

## See Also

### Managing context hierarchy
- [var parent: CLSContext?](./parent.md)
  The direct ancestor of this context.
- [func removeFromParent()](./removefromparent%28%29.md)
  Removes the context from its parent.
- [func addChildContext(CLSContext)](./addchildcontext%28_%29.md)
  Adds the specifed context as a child of the context receiving the method call.
- [func descendant(matchingIdentifierPath: [String], completion: (CLSContext?, (any Error)?) -> Void)](./descendant%28matchingidentifierpath,completion%29.md)
  Finds the context with the given identifier path relative to this context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/classkit/clscontext/identifierpath)*