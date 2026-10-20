# documentType(forIdentifier:)

**Framework**: HealthKit  
**Kind**: method  
**Role**: Type Method

Returns the shared document type for the provided identifier.

**Availability**:
- iOS 10.0+ - Deprecated in 27.2
- iPadOS 10.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.2
- macOS 13.0+
- visionOS 1.0+ - Deprecated in 27.2
- watchOS 3.0+ - Deprecated in 27.2

## Declaration

```swift
class func documentType(forIdentifier identifier: HKDocumentTypeIdentifier) -> HKDocumentType?
```

```objc
+ (HKDocumentType *) documentTypeForIdentifier:(HKDocumentTypeIdentifier) identifier;
```

#### Return Value

The shared [`HKDocumentType`](../hkdocumenttype.md) instance based on the provided identifier.

#### Discussion

This method returns an instance of the [`HKQuantityType`](../hkquantitytype.md) concrete subclass. HealthKit uses document types to manage medical documents. Use document type instances to create document samples that you can save in the HealthKit store. For more information, see [`HKDocumentSample`](../hkdocumentsample.md).

## Parameters

- `identifier`: A document type identifier. For a list of valid identifiers, see [`HKDocumentTypeIdentifier`](../hkdocumenttypeidentifier.md).

## See Also

### Creating document types
- [struct HKDocumentTypeIdentifier](../hkdocumenttypeidentifier.md)
  The identifiers for documents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkobjecttype/documenttype(foridentifier:))*