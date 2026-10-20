# nodeDetails(forKeys:)

**Framework**: Open Directory  
**Kind**: method  
**Role**: Instance Method

Returns a dictionary containing details about a node.

**Availability**:
- Mac Catalyst
- macOS 10.6+

## Declaration

```swift
func nodeDetails(forKeys inKeys: [Any]!) throws -> [AnyHashable : Any]
```

```objc
- (NSDictionary *) nodeDetailsForKeys:(NSArray *) inKeys error:(NSError **) outError;
```

#### Return Value

A dictionary containing details about the node corresponding to keys specified by `inKeys`.

#### Discussion

> **Handling Errors in Swift**:  In Swift, this method returns a nonoptional result and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `inKeys`: An array of keys corresponding to the values returned in the dictionary.

## See Also

### Querying a Node
- [func customCall(Int, send: Data!) throws -> Data](./customcall%28_,send%29.md)
  Returns the result of a custom call to the node.
- [var nodeName: String!](./nodename.md)
  The node’s name.
- [func subnodeNames() throws -> [Any]](./subnodenames%28%29.md)
  Returns the names of subnodes for the node.
- [func unreachableSubnodeNames() throws -> [Any]](./unreachablesubnodenames%28%29.md)
  Returns an array of the subnodes of a given node that are currently unreachable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/opendirectory/odnode/nodedetails(forkeys:))*