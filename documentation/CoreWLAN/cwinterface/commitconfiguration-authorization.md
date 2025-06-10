# commitConfiguration(_:authorization:)

**Framework**: Core WLAN  
**Kind**: method

Commit a configuration for the given WLAN interface.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func commitConfiguration(_ configuration: CWConfiguration, authorization: SFAuthorization?) throws
```

#### Discussion

This method requires the caller have root privileges or obtain administrator privileges with the  parameter.

> **Note**:  In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure. You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `configuration`: The configuration to commit.
- `authorization`: An SFAuthorization object to use for authorizing the commit. This parameter is optional and can be passed as  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/corewlan/cwinterface/commitconfiguration(_:authorization:))*