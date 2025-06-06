# HKCDADocument

**Framework**: HealthKit  
**Kind**: class

An object representing a Clinical Document Architecture (CDA) document in HealthKit.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class HKCDADocument
```

#### Overview

CDA documents use XML to encode clinical documents so that they can be easily exchanged. For more information on the CDA document format, see the [`Clinical Document Architecture, R2`](https://developer.apple.comhttp://www.hl7.org/implement/standards/product_brief.cfm?product_id=7) standard.

Do not instantiate `HKCDADocument` objects directly. Instead, create a new [`HKCDADocumentSample`](hkcdadocumentsample.md) object by calling the  [`init(data:start:end:metadata:)`](hkcdadocumentsample/init(data:start:end:metadata:).md) method, and passing the CDA’s XML data. HealthKit creates a `HKCDADocument` object for the XML, and assigns it to the sample’s [`document`](hkcdadocumentsample/document.md) property.

`HKCDADocument` objects are immutable. When you create a new document sample, HealthKit parses the title, patient name, author name, and custodian name from the XML to populates the document object’s properties. These properties cannot be changed.

Like many HealthKit classes, the [`HKCDADocument`](hkcdadocument.md) class should not be subclassed.

## Topics

### Accessing the Document’s Data
- [var authorName: String](hkcdadocument/authorname.md)
  The document’s author.
- [var custodianName: String](hkcdadocument/custodianname.md)
  The name of the organization responsible for the document.
- [var documentData: Data?](hkcdadocument/documentdata.md)
  The CDA document stored as XML data.
- [var patientName: String](hkcdadocument/patientname.md)
  The patient’s name.
- [var title: String](hkcdadocument/title.md)
  The document’s title.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var document: HKCDADocument?](hkcdadocumentsample/document.md)
  The CDA document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkcdadocument)*