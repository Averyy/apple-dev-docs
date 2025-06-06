# jsonObject(with:options:)

**Framework**: Foundation  
**Kind**: method

Returns a Foundation object from JSON data in a given stream.

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
class func jsonObject(with stream: InputStream, options opt: JSONSerialization.ReadingOptions = []) throws -> Any
```

#### Return Value

A Foundation object from the JSON data in `stream`.

#### Discussion

The data in the stream must be in one of the 5 supported encodings listed in the JSON specification: UTF-8, UTF-16LE, UTF-16BE, UTF-32LE, UTF-32BE. The data may or may not have a BOM. The most efficient encoding to use for parsing is UTF-8, so if you have a choice in encoding the data passed to this method, use UTF-8.

> **Note**:  In Swift, this method returns a nonoptional result and is marked with the `throws` keyword to indicate that it throws an error in cases of failure. You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `stream`: The stream should be open and configured.
- `opt`: For possible values, see  .

## See Also

- [class func writeJSONObject(Any, to: OutputStream, options: JSONSerialization.WritingOptions, error: NSErrorPointer) -> Int](jsonserialization/writejsonobject(_:to:options:error:).md)
  Writes a given JSON object to a stream.
- [class func jsonObject(with: Data, options: JSONSerialization.ReadingOptions) throws -> Any](jsonserialization/jsonobject(with:options:)-8demi.md)
  Returns a Foundation object from given JSON data.
- [JSONSerialization.ReadingOptions](jsonserialization/readingoptions.md)
  Options used when creating Foundation objects from JSON data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/jsonserialization/jsonobject(with:options:)-3afap)*