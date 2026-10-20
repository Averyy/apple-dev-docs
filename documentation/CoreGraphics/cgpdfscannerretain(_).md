# CGPDFScannerRetain(_:)

**Framework**: Core Graphics  
**Kind**: func  
**Role**: Function

Increments the retain count of a scanner object.

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
func CGPDFScannerRetain(_ scanner: CGPDFScannerRef) -> CGPDFScannerRef
```

```c
extern CGPDFScannerRefCGPDFScannerRetain(CGPDFScannerRef scanner);
```

#### Return Value

The same scanner object passed to the function in the `scanner` parameter.

## Parameters

- `scanner`: The scanner object to retain.

## See Also

### Retaining and Releasing PDF Scanner Objects
- [func CGPDFScannerRelease(CGPDFScannerRef)](./cgpdfscannerrelease%28_%29.md)
  Decrements the retain count of a scanner object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpdfscannerretain(_:))*