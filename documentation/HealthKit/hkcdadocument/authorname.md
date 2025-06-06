# authorName

**Framework**: HealthKit  
**Kind**: property

The document’s author.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var authorName: String { get }
```

#### Discussion

Usually, this is the treating physician’s name.

HealthKit automatically extracts the author’s name from the CDA’s XML data.

## See Also

- [var custodianName: String](hkcdadocument/custodianname.md)
  The name of the organization responsible for the document.
- [var documentData: Data?](hkcdadocument/documentdata.md)
  The CDA document stored as XML data.
- [var patientName: String](hkcdadocument/patientname.md)
  The patient’s name.
- [var title: String](hkcdadocument/title.md)
  The document’s title.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkcdadocument/authorname)*