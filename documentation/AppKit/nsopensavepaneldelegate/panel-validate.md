# panel(_:validate:)

**Framework**: AppKit  
**Kind**: method

Asks the delegate to validate the URL for a file that the user selected.

**Availability**:
- macOS 10.6+

## Declaration

```swift
@MainActor
optional func panel(_ sender: Any, validate url: URL) throws
```

#### Discussion

Save panels call this method when the user clicks the Save button. Open panels call it when the user clicks the Open button. An Open panel calls this method once for each selected filename or directory.

> **Note**:  In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure. You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

 In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.

You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `sender`: The panel that requests URL validation.
- `url`: The URL for you to validate.

## See Also

- [func panel(Any, shouldEnable: URL) -> Bool](nsopensavepaneldelegate/panel(_:shouldenable:).md)
  Asks the delegate whether the specified URL should be enabled in the Open panel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsopensavepaneldelegate/panel(_:validate:))*