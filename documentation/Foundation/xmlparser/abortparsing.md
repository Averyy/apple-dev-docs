# abortParsing()

**Framework**: Foundation  
**Kind**: method

Stops the parser object.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func abortParsing()
```

#### Discussion

If you invoke this method, the delegate, if it implements [`parser(_:parseErrorOccurred:)`](xmlparserdelegate/parser(_:parseerroroccurred:).md), is informed of the cancelled parsing operation.

## See Also

- [func parse() -> Bool](xmlparser/parse.md)
  Starts the event-driven parsing operation.
- [var parserError: (any Error)?](xmlparser/parsererror.md)
  An [`NSError`](nserror.md) object from which you can obtain information about a parsing error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmlparser/abortparsing())*