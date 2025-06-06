# CGPDFOperatorTableRetain(_:)

**Framework**: Core Graphics  
**Kind**: func

Increments the retain count of a CGPDFOperatorTable object.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func CGPDFOperatorTableRetain(_ table: CGPDFOperatorTableRef) -> CGPDFOperatorTableRef
```

#### Return Value

The same PDF operator table you passed in as the `table` parameter.

## Parameters

- `table`: A PDF operator table.

## See Also

- [func CGPDFOperatorTableRelease(CGPDFOperatorTableRef)](cgpdfoperatortablerelease(_:).md)
  Decrements the retain count of a CGPDFOperatorTable object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpdfoperatortableretain(_:))*