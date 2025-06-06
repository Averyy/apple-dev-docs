# data(withJSONObject:options:)

**Framework**: Foundation  
**Kind**: method

Returns JSON data from a Foundation object.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class func data(withJSONObject obj: Any, options opt: JSONSerialization.WritingOptions = []) throws -> Data
```

#### Return Value

JSON data for `obj`, or `nil` if an internal error occurs. The resulting data is encoded in UTF-8.

#### Discussion

If `obj` can’t produce valid JSON, [`JSONSerialization`](jsonserialization.md) throws an exception. This exception occurs prior to parsing and represents a programming error, not an internal error. Before calling this method, you should check whether the input can produce valid JSON by using [`isValidJSONObject(_:)`](jsonserialization/isvalidjsonobject(_:).md).

Setting the [`prettyPrinted`](jsonserialization/writingoptions/prettyprinted.md) option generates JSON with white space designed to make the output more readable. If this option isn’t set, [`JSONSerialization`](jsonserialization.md) generates the most compact possible JSON.

> **Note**:  In Swift, this method returns a nonoptional result and is marked with the `throws` keyword to indicate that it throws an error in cases of failure. You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

 In Swift, this method returns a nonoptional result and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.

You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `obj`: The object from which to generate JSON data. Must not be  .
- `opt`: See   for possible values.

## See Also

- [class func writeJSONObject(Any, to: OutputStream, options: JSONSerialization.WritingOptions, error: NSErrorPointer) -> Int](jsonserialization/writejsonobject(_:to:options:error:).md)
  Writes a given JSON object to a stream.
- [JSONSerialization.WritingOptions](jsonserialization/writingoptions.md)
  Options for writing JSON data.
- [class func isValidJSONObject(Any) -> Bool](jsonserialization/isvalidjsonobject(_:).md)
  Returns a Boolean value that indicates whether the serializer can convert a given object to JSON data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/jsonserialization/data(withjsonobject:options:))*