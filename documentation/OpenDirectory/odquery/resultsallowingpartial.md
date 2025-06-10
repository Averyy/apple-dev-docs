# resultsAllowingPartial(_:)

**Framework**: Open Directory  
**Kind**: method

Returns results from a query synchronously.

**Availability**:
- Mac Catalyst ?+
- macOS 10.6+

## Declaration

```swift
func resultsAllowingPartial(_ inAllowPartialResults: Bool) throws -> [Any]
```

#### Return Value

The results of the query in an array of `ODRecord` objects.

#### Discussion

> **Note**:  In Swift, this method returns a nonoptional result and is marked with the `throws` keyword to indicate that it throws an error in cases of failure. You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `inAllowPartialResults`: If  , only immediately available results are returned; otherwise, the function waits until all results are available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/opendirectory/odquery/resultsallowingpartial(_:))*