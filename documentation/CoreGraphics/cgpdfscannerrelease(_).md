# CGPDFScannerRelease(_:)

**Framework**: Core Graphics  
**Kind**: func  
**Role**: Function

Decrements the retain count of a scanner object.

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
func CGPDFScannerRelease(_ scanner: CGPDFScannerRef)
```

```c
extern void CGPDFScannerRelease(CGPDFScannerRef scanner);
```

## Parameters

- `scanner`: The scanner object to release.

## See Also

### Retaining and Releasing PDF Scanner Objects
- [func CGPDFScannerRetain(CGPDFScannerRef) -> CGPDFScannerRef](./cgpdfscannerretain%28_%29.md)
  Increments the retain count of a scanner object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpdfscannerrelease(_:))*