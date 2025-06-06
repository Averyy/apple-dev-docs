# patientName

**Framework**: HealthKit  
**Kind**: property

The patient’s name.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var patientName: String { get }
```

#### Discussion

HealthKit automatically extracts the patient’s name from the CDA’s XML data.

## See Also

- [var authorName: String](hkcdadocument/authorname.md)
  The document’s author.
- [var custodianName: String](hkcdadocument/custodianname.md)
  The name of the organization responsible for the document.
- [var documentData: Data?](hkcdadocument/documentdata.md)
  The CDA document stored as XML data.
- [var title: String](hkcdadocument/title.md)
  The document’s title.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkcdadocument/patientname)*