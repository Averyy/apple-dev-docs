# propertyList(from:options:format:)

**Framework**: Foundation  
**Kind**: method

Creates and returns a property list from the specified data.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class func propertyList(from data: Data, options opt: PropertyListSerialization.ReadOptions = [], format: UnsafeMutablePointer<PropertyListSerialization.PropertyListFormat>?) throws -> Any
```

#### Return Value

A property list object corresponding to the representation in `data`. If data is not in a supported format, returns `nil`.

#### Discussion

> **Note**:  In Swift, this method returns a nonoptional result and is marked with the `throws` keyword to indicate that it throws an error in cases of failure. You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

 In Swift, this method returns a nonoptional result and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.

You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `data`: A data object containing a serialized property list.
- `opt`: The options used to create the property list. For possible values, see  .
- `format`: Upon return, contains the format that the property list was stored in. Pass   if you do not need to know the format.

## See Also

- [class func propertyList(with: InputStream, options: PropertyListSerialization.ReadOptions, format: UnsafeMutablePointer<PropertyListSerialization.PropertyListFormat>?) throws -> Any](propertylistserialization/propertylist(with:options:format:).md)
  Creates and returns a property list by reading from the specified stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/propertylistserialization/propertylist(from:options:format:))*