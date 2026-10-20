# init(session:name:)

**Framework**: Open Directory  
**Kind**: init  
**Role**: Initializer

Creates a node object with a specified session and name.

**Availability**:
- Mac Catalyst
- macOS 10.6+

## Declaration

```swift
init(session inSession: ODSession!, name inName: String!) throws
```

```objc
- (instancetype) initWithSession:(ODSession *) inSession name:(NSString *) inName error:(NSError **) outError;
```

#### Return Value

The created node object.

#### Discussion

> **Handling Errors in Swift**:  In Swift, this API is imported as an initializer and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `inSession`: The session.
- `inName`: The name of the node.

## See Also

### Creating and Initializing a Node
- [init(session: ODSession!, type: ODNodeType) throws](./init%28session,type%29.md)
  Creates a node object with a specified session and type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/opendirectory/odnode/init(session:name:))*