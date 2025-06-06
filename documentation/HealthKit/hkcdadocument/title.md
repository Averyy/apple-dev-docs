# title

**Framework**: HealthKit  
**Kind**: property

The document’s title.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var title: String { get }
```

#### Discussion

HealthKit automatically extracts the document’s title from the CDA’s XML data.

## See Also

- [var authorName: String](hkcdadocument/authorname.md)
  The document’s author.
- [var custodianName: String](hkcdadocument/custodianname.md)
  The name of the organization responsible for the document.
- [var documentData: Data?](hkcdadocument/documentdata.md)
  The CDA document stored as XML data.
- [var patientName: String](hkcdadocument/patientname.md)
  The patient’s name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkcdadocument/title)*