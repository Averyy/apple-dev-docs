# data(from:documentAttributes:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns a data object that contains a text stream corresponding to the characters and attributes within the specified range.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func data(from range: NSRange, documentAttributes dict: [NSAttributedString.DocumentAttributeKey : Any] = [:]) throws -> Data
```

```objc
- (NSData *) dataFromRange:(NSRange) range documentAttributes:(NSDictionary<NSString *,id> *) dict error:(NSError **) error;
```

## Return Value

Returns the data for the attributed string, or `nil` if failure. When `nil`, `error` encapsulates the error information.

## Discussion

Raises an [`rangeException`](../nsexceptionname/rangeexception.md) if any part of `range` lies beyond the end of the receiver’s characters.

> **Handling Errors in Swift**:  In Swift, this method returns a nonoptional result and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `range`: The range.
- `dict`: A required dictionary specifying the document attributes. The dictionary contains values from `Document Types` and must at least contain [`documentType`](./documentattributekey/documenttype.md).

## See Also

### Exporting the string as data
- [func fileWrapper(from: NSRange, documentAttributes: [NSAttributedString.DocumentAttributeKey : Any]) throws -> FileWrapper](./filewrapper%28from,documentattributes%29.md)
  Returns a file wrapper object that contains a text stream corresponding to the characters and attributes within the specified range.
- [func docFormat(from: NSRange, documentAttributes: [NSAttributedString.DocumentAttributeKey : Any]) -> Data?](./docformat%28from,documentattributes%29.md)
  Returns a data object that contains a Microsoft Word–format stream corresponding to the characters and attributes within the specified range.
- [func rtf(from: NSRange, documentAttributes: [NSAttributedString.DocumentAttributeKey : Any]) -> Data?](./rtf%28from,documentattributes%29.md)
  Returns a data object that contains an RTF stream corresponding to the characters and attributes within the specified range, omitting all attachment attributes.
- [func rtfd(from: NSRange, documentAttributes: [NSAttributedString.DocumentAttributeKey : Any]) -> Data?](./rtfd%28from,documentattributes%29.md)
  Returns a data object that contains an RTFD stream corresponding to the characters and attributes within the specified range.
- [func rtfdFileWrapper(from: NSRange, documentAttributes: [NSAttributedString.DocumentAttributeKey : Any]) -> FileWrapper?](./rtfdfilewrapper%28from,documentattributes%29.md)
  Returns a file wrapper object that contains an RTFD document corresponding to the characters and attributes within the specified range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstring/data(from:documentattributes:))*