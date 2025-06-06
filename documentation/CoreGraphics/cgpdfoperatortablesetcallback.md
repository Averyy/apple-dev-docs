# CGPDFOperatorTableSetCallback(_:_:_:)

**Framework**: Core Graphics  
**Kind**: func

Sets a callback function for a PDF operator.

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
func CGPDFOperatorTableSetCallback(_ table: CGPDFOperatorTableRef, _ name: UnsafePointer<CChar>, _ callback: CGPDFOperatorCallback)
```

#### Discussion

You call the function [`CGPDFOperatorTableSetCallback(_:_:_:)`](cgpdfoperatortablesetcallback(_:_:_:).md) for each PDF operator for which you want to provide a callback. See Appendix A in the , version 1.3, Adobe Systems Incorporated for a summary of PDF operators.

## Parameters

- `table`: A PDF operator table.
- `name`: The name of the PDF operator you want to set a callback for.
- `callback`: The callback to invoke for the PDF operator specified by the   parameter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpdfoperatortablesetcallback(_:_:_:))*