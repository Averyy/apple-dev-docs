# CGPDFOperatorTableRetain(_:)

**Framework**: Core Graphics  
**Kind**: func  
**Role**: Function

Increments the retain count of a CGPDFOperatorTable object.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func CGPDFOperatorTableRetain(_ table: CGPDFOperatorTableRef) -> CGPDFOperatorTableRef
```

```c
extern CGPDFOperatorTableRefCGPDFOperatorTableRetain(CGPDFOperatorTableRef table);
```

## Return Value

The same PDF operator table you passed in as the `table` parameter.

## Parameters

- `table`: A PDF operator table.

## See Also

### Retaining and Releasing a PDF Operator Table
- [func CGPDFOperatorTableRelease(CGPDFOperatorTableRef)](./cgpdfoperatortablerelease%28_%29.md)
  Decrements the retain count of a CGPDFOperatorTable object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpdfoperatortableretain(_:))*