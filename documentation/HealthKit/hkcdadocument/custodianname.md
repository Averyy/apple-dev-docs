# custodianName

**Framework**: HealthKit  
**Kind**: property

The name of the organization responsible for the document.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var custodianName: String { get }
```

#### Discussion

Usually, this is the treating institution’s name.

HealthKit automatically extracts the custodian’s name from the CDA’s XML data.

## See Also

- [var authorName: String](hkcdadocument/authorname.md)
  The document’s author.
- [var documentData: Data?](hkcdadocument/documentdata.md)
  The CDA document stored as XML data.
- [var patientName: String](hkcdadocument/patientname.md)
  The patient’s name.
- [var title: String](hkcdadocument/title.md)
  The document’s title.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkcdadocument/custodianname)*