# init(contentsOf:)

**Framework**: Automator  
**Kind**: init

Creates and initializes a workflow based on the contents of the specified file.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.4+

## Declaration

```swift
convenience init(contentsOf fileURL: URL) throws
```

#### Return Value

The initialized workflow object. On error, returns nil.

#### Discussion

> **Note**:  In Swift, this method returns a nonoptional result and is marked with the `throws` keyword to indicate that it throws an error in cases of failure. You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

 In Swift, this method returns a nonoptional result and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.

You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `fileURL`: URL that specifies the location of a workflow file.

## See Also

- [init()](amworkflow/init.md)
  Creates and initializes a workflow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automator/amworkflow/init(contentsof:))*