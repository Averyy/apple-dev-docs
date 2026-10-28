# subnodeNames()

**Framework**: Open Directory  
**Kind**: method  
**Role**: Instance Method

Returns the names of subnodes for the node.

**Availability**:
- Mac Catalyst
- macOS 10.6+

## Declaration

```swift
func subnodeNames() throws -> [Any]
```

```objc
- (NSArray *) subnodeNamesAndReturnError:(NSError **) outError;
```

## Return Value

An array of subnode names.

## Discussion

> **Handling Errors in Swift**:  In Swift, this method returns a nonoptional result and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## See Also

### Querying a Node
- [func customCall(Int, send: Data!) throws -> Data](./customcall%28_,send%29.md)
  Returns the result of a custom call to the node.
- [func nodeDetails(forKeys: [Any]!) throws -> [AnyHashable : Any]](./nodedetails%28forkeys%29.md)
  Returns a dictionary containing details about a node.
- [var nodeName: String!](./nodename.md)
  The node’s name.
- [func unreachableSubnodeNames() throws -> [Any]](./unreachablesubnodenames%28%29.md)
  Returns an array of the subnodes of a given node that are currently unreachable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/opendirectory/odnode/subnodenames())*