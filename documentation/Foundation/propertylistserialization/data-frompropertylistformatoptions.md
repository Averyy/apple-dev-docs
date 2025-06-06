# data(fromPropertyList:format:options:)

**Framework**: Foundation  
**Kind**: method

Returns an `NSData` object containing a given property list in a specified format.

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
class func data(fromPropertyList plist: Any, format: PropertyListSerialization.PropertyListFormat, options opt: PropertyListSerialization.WriteOptions) throws -> Data
```

#### Return Value

An `NSData` object containing `plist` in the format specified by `format`.

#### Discussion

> **Note**:  In Swift, this method returns a nonoptional result and is marked with the `throws` keyword to indicate that it throws an error in cases of failure. You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

 In Swift, this method returns a nonoptional result and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.

You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `plist`: A property list object.
- `format`: A property list format. For possible values, see  .
- `opt`: The   parameter is currently unused. No options should be specified.

## See Also

- [Archives and Serializations Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Archiving/Archiving.html#//apple_ref/doc/uid/10000047i)
- [Property List Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/PropertyLists/Introduction/Introduction.html#//apple_ref/doc/uid/10000048i)
- [class func writePropertyList(Any, to: OutputStream, format: PropertyListSerialization.PropertyListFormat, options: PropertyListSerialization.WriteOptions, error: NSErrorPointer) -> Int](propertylistserialization/writepropertylist(_:to:format:options:error:).md)
  Writes a property list to the specified stream.
- [PropertyListSerialization.WriteOptions](propertylistserialization/writeoptions.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/propertylistserialization/data(frompropertylist:format:options:))*