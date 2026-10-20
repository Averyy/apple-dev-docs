# columnNumber

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The column number of the XML document being processed by the parser.

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
var columnNumber: Int { get }
```

```objc
@property (readonly) NSInteger columnNumber;
```

#### Discussion

The column refers to the nesting level of the XML elements in the document. You may access this property once a parsing operation has begun or after an error occurs.

## See Also

### Obtaining Parser State
- [var lineNumber: Int](./linenumber.md)
  The line number of the XML document being processed by the parser.
- [var publicID: String?](./publicid.md)
  The public identifier of the external entity referenced in the XML document.
- [var systemID: String?](./systemid.md)
  The system identifier of the external entity referenced in the XML document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmlparser/columnnumber)*