# nodeNames()

**Framework**: Open Directory  
**Kind**: method  
**Role**: Instance Method

Returns the node names that are registered with this session.

**Availability**:
- Mac Catalyst
- macOS 10.6+

## Declaration

```swift
func nodeNames() throws -> [Any]
```

```objc
- (NSArray *) nodeNamesAndReturnError:(NSError **) outError;
```

## Return Value

The node names registered with this session.

## Discussion

> **Handling Errors in Swift**:  In Swift, this method returns a nonoptional result and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/opendirectory/odsession/nodenames())*