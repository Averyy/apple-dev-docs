# resultsAllowingPartial(_:)

**Framework**: Open Directory  
**Kind**: method  
**Role**: Instance Method

Returns results from a query synchronously.

**Availability**:
- Mac Catalyst
- macOS 10.6+

## Declaration

```swift
func resultsAllowingPartial(_ inAllowPartialResults: Bool) throws -> [Any]
```

```objc
- (NSArray *) resultsAllowingPartial:(BOOL) inAllowPartialResults error:(NSError **) outError;
```

## Return Value

The results of the query in an array of `ODRecord` objects.

## Discussion

> **Handling Errors in Swift**:  In Swift, this method returns a nonoptional result and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `inAllowPartialResults`: If [`true`](../../Swift/true.md), only immediately available results are returned; otherwise, the function waits until all results are available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/opendirectory/odquery/resultsallowingpartial(_:))*