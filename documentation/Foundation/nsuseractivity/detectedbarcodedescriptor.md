# detectedBarcodeDescriptor

**Framework**: Foundation  
**Kind**: property

The barcode that the system scanner passes in.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 13.1+
- macOS 10.13.4+
- tvOS 11.3+
- visionOS 1.0+

## Declaration

```swift
@NSCopying
var detectedBarcodeDescriptor: CIBarcodeDescriptor? { get }
```

#### Discussion

This property is optional. This value is present if the user activity was created from a source that detected a barcode or a QR code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsuseractivity/detectedbarcodedescriptor)*