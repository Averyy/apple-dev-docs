# parse()

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Starts the event-driven parsing operation.

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
func parse() -> Bool
```

```objc
- (BOOL) parse;
```

## Return Value

[`true`](../../Swift/true.md) if the parsing operation succeeds; [`false`](../../Swift/false.md) if an error occurs or if the parsing operation aborts.

## See Also

### Parsing
- [func abortParsing()](./abortparsing%28%29.md)
  Stops the parser object.
- [var parserError: (any Error)?](./parsererror.md)
  An [`NSError`](../nserror.md) object from which you can obtain information about a parsing error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmlparser/parse())*