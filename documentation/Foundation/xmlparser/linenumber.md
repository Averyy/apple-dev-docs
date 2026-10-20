# lineNumber

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The line number of the XML document being processed by the parser.

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
var lineNumber: Int { get }
```

```objc
@property (readonly) NSInteger lineNumber;
```

#### Discussion

You may access this property once a parsing operation has begun or after an error occurs.

## See Also

### Obtaining Parser State
- [var columnNumber: Int](./columnnumber.md)
  The column number of the XML document being processed by the parser.
- [var publicID: String?](./publicid.md)
  The public identifier of the external entity referenced in the XML document.
- [var systemID: String?](./systemid.md)
  The system identifier of the external entity referenced in the XML document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmlparser/linenumber)*