# CGPDFOperatorTableRelease(_:)

**Framework**: Core Graphics  
**Kind**: func  
**Role**: Function

Decrements the retain count of a CGPDFOperatorTable object.

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
func CGPDFOperatorTableRelease(_ table: CGPDFOperatorTableRef)
```

```c
extern void CGPDFOperatorTableRelease(CGPDFOperatorTableRef table);
```

## Parameters

- `table`: A PDF operator table.

## See Also

### Retaining and Releasing a PDF Operator Table
- [func CGPDFOperatorTableRetain(CGPDFOperatorTableRef) -> CGPDFOperatorTableRef](./cgpdfoperatortableretain%28_%29.md)
  Increments the retain count of a CGPDFOperatorTable object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpdfoperatortablerelease(_:))*