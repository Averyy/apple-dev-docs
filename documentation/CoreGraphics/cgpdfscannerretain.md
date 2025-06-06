# CGPDFScannerRetain(_:)

**Framework**: Core Graphics  
**Kind**: func

Increments the retain count of a scanner object.

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
func CGPDFScannerRetain(_ scanner: CGPDFScannerRef) -> CGPDFScannerRef
```

#### Return Value

The same scanner object passed to the function in the `scanner` parameter.

## Parameters

- `scanner`: The scanner object to retain.

## See Also

- [func CGPDFScannerRelease(CGPDFScannerRef)](cgpdfscannerrelease(_:).md)
  Decrements the retain count of a scanner object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpdfscannerretain(_:))*