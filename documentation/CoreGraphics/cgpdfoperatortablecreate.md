# CGPDFOperatorTableCreate()

**Framework**: Core Graphics  
**Kind**: func

Creates an empty PDF operator table.

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
func CGPDFOperatorTableCreate() -> CGPDFOperatorTableRef?
```

#### Return Value

An empty PDF operator table. In Objective-C, you’re responsible for releasing this object by calling [`CGPDFOperatorTableRelease(_:)`](cgpdfoperatortablerelease(_:).md).

#### Discussion

Call the function [`CGPDFOperatorTableSetCallback(_:_:_:)`](cgpdfoperatortablesetcallback(_:_:_:).md) to fill the operator table with callbacks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpdfoperatortablecreate())*