# propertyList(with:options:format:)

**Framework**: Foundation  
**Kind**: method

Creates and returns a property list by reading from the specified stream.

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
class func propertyList(with stream: InputStream, options opt: PropertyListSerialization.ReadOptions = [], format: UnsafeMutablePointer<PropertyListSerialization.PropertyListFormat>?) throws -> Any
```

#### Return Value

A property list object corresponding to the representation in `data`. If data is not in a supported format, returns `nil`.

#### Discussion

> **Note**:  In Swift, this method returns a nonoptional result and is marked with the `throws` keyword to indicate that it throws an error in cases of failure. You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `stream`: An   object. The stream should be open and configured for reading.
- `opt`: The options used to create the property list. For possible values, see  .
- `format`: Upon return, contains the format that the property list was stored in. Pass   if you do not need to know the format.

## See Also

- [class func propertyList(from: Data, options: PropertyListSerialization.ReadOptions, format: UnsafeMutablePointer<PropertyListSerialization.PropertyListFormat>?) throws -> Any](propertylistserialization/propertylist(from:options:format:).md)
  Creates and returns a property list from the specified data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/propertylistserialization/propertylist(with:options:format:))*