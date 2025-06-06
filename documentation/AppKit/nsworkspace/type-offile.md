# type(ofFile:)

**Framework**: AppKit  
**Kind**: method

Returns the uniform type identifier of the specified file, if it can be determined.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func type(ofFile absoluteFilePath: String) throws -> String
```

#### Return Value

An `NSString` containing the uniform type identifier of the file at `absoluteFilePath`. If no UTI can be determined the return value is `nil`.

#### Discussion

If the file at the specified path is a symbolic link, the type of the symbolic link is returned.

You can safely call this method from any thread of your app.

> **Note**:  In Swift, this method returns a nonoptional result and is marked with the `throws` keyword to indicate that it throws an error in cases of failure. You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

 In Swift, this method returns a nonoptional result and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.

You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `absoluteFilePath`: The absolute path of the file.

## See Also

- [func localizedDescription(forType: String) -> String?](nsworkspace/localizeddescription(fortype:).md)
  Returns the localized description for the specified Uniform Type Identifier (UTI).
- [func preferredFilenameExtension(forType: String) -> String?](nsworkspace/preferredfilenameextension(fortype:).md)
  Returns the preferred filename extension for the specified Uniform Type Identifier (UTI).
- [func filenameExtension(String, isValidForType: String) -> Bool](nsworkspace/filenameextension(_:isvalidfortype:).md)
  Returns whether the specified filename extension is appropriate for the Uniform Type Identifier (UTI).
- [func type(String, conformsToType: String) -> Bool](nsworkspace/type(_:conformstotype:).md)
  Returns a Boolean indicating that the first Uniform Type Identifier (UTI) conforms to the second UTI.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsworkspace/type(offile:))*