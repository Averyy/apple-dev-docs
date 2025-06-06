# write(to:)

**Framework**: Automator  
**Kind**: method

Writes the workflow to the specified file.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.4+

## Declaration

```swift
func write(to fileURL: URL) throws
```

#### Discussion

You might want to save the workflow, for example, because you have made changes to a variable it contains.

> **Note**:  In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure. You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `fileURL`: URL that specifies the file location to write the workflow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automator/amworkflow/write(to:))*