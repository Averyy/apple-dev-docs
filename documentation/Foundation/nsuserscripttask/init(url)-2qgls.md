# init(url:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Return a user script task instance given a URL for a script file.

**Availability**:
- macOS 10.8+

## Declaration

```swift
init(url: URL) throws
```

```objc
- (instancetype) initWithURL:(NSURL *) url error:(NSError **) error;
```

## Return Value

An instance of an `NSUserScriptTask` subclass or `nil` if the file does not appear to match any of the known types.

## Discussion

The returned object will be of one of the specific sub-classes ([`NSUserUnixTask`](../nsuserunixtask.md), [`NSUserAppleScriptTask`](../nsuserapplescripttask.md), and [`NSUserAutomatorTask`](../nsuserautomatortask.md)), or `nil` if the file does not appear to match any of the known types.

If invoked from a subclass, the result will be that class or `nil`.

> **Handling Errors in Swift**:  In Swift, this API is imported as an initializer and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `url`: The script URL.

## See Also

### Specifying the Script
- [var scriptURL: URL](./scripturl.md)
  The URL of the script file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsuserscripttask/init(url:)-2qgls)*