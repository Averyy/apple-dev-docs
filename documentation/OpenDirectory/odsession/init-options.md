# init(options:)

**Framework**: Open Directory  
**Kind**: init

Creates a session object directed over proxy to another host.

**Availability**:
- Mac Catalyst ?+
- macOS 10.6+

## Declaration

```swift
init(options inOptions: [AnyHashable : Any]! = [:]) throws
```

#### Return Value

The created session object.

#### Discussion

> **Note**:  In Swift, this API is imported as an initializer and is marked with the `throws` keyword to indicate that it throws an error in cases of failure. You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

 In Swift, this API is imported as an initializer and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.

You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `inOptions`: A dictionary of options to associate with the session. Can be  .

## See Also

- [class ODSession](odsession.md)
  An `ODSession` object serves as a Cocoa wrapper for an Open Directory session.
- [class func `default`() -> ODSession!](odsession/default.md)
  Returns a shared instance of the local session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/opendirectory/odsession/init(options:))*