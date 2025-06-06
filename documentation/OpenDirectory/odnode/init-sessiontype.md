# init(session:type:)

**Framework**: Opendirectory  
**Kind**: init

Creates a node object with a specified session and type.

**Availability**:
- Mac Catalyst ?+
- macOS 10.6+

## Declaration

```swift
init(session inSession: ODSession!, type inType: ODNodeType) throws
```

#### Return Value

The created node object.

#### Discussion

> **Note**:  In Swift, this API is imported as an initializer and is marked with the `throws` keyword to indicate that it throws an error in cases of failure. You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `inSession`: The session.
- `inType`: The node type.

## See Also

- [init(session: ODSession!, name: String!) throws](odnode/init(session:name:).md)
  Creates a node object with a specified session and name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/opendirectory/odnode/init(session:type:))*