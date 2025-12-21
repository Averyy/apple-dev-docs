# execute(_:)

**Framework**: Contacts  
**Kind**: method

Executes a save request and returns success or failure.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
func execute(_ saveRequest: CNSaveRequest) throws
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the save request executes successfully; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

It is recommended that you do not access objects in the save request from other threads when it is in the process of being executed, because it may modify the contacts in the process. A save request only applies the changes to the objects. If there are overlapping changes with multiple or concurrent [`CNSaveRequest`](cnsaverequest.md) then the last saved change wins.

> **Note**: In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure. You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and [`About Imported Cocoa Error Parameters`](https://developer.apple.com/documentation/Swift/about-imported-cocoa-error-parameters).

## Parameters

- `saveRequest`: The save request to execute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cncontactstore/execute(_:))*