# nodeDetails(forKeys:)

**Framework**: Open Directory  
**Kind**: method

Returns a dictionary containing details about a node.

**Availability**:
- Mac Catalyst ?+
- macOS 10.6+

## Declaration

```swift
func nodeDetails(forKeys inKeys: [Any]!) throws -> [AnyHashable : Any]
```

#### Return Value

A dictionary containing details about the node corresponding to keys specified by `inKeys`.

#### Discussion

> **Note**:  In Swift, this method returns a nonoptional result and is marked with the `throws` keyword to indicate that it throws an error in cases of failure. You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `inKeys`: An array of keys corresponding to the values returned in the dictionary.

## See Also

- [func customCall(Int, send: Data!) throws -> Data](odnode/customcall(_:send:).md)
  Returns the result of a custom call to the node.
- [var nodeName: String!](odnode/nodename.md)
  The node’s name.
- [func subnodeNames() throws -> [Any]](odnode/subnodenames.md)
  Returns the names of subnodes for the node.
- [func unreachableSubnodeNames() throws -> [Any]](odnode/unreachablesubnodenames.md)
  Returns an array of the subnodes of a given node that are currently unreachable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/opendirectory/odnode/nodedetails(forkeys:))*