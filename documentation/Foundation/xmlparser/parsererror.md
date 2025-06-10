# parserError

**Framework**: Foundation  
**Kind**: property

An [`NSError`](nserror.md) object from which you can obtain information about a parsing error.

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
var parserError: (any Error)? { get }
```

#### Discussion

You may access this property after a parsing operation abnormally terminates to determine the cause of error.

## See Also

- [func parse() -> Bool](xmlparser/parse.md)
  Starts the event-driven parsing operation.
- [func abortParsing()](xmlparser/abortparsing.md)
  Stops the parser object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmlparser/parsererror)*