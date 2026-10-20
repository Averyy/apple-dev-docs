# custodianName

**Framework**: HealthKit  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (copy, readonly) NSString * custodianName;
```

#### Discussion

Usually, this is the treating institution’s name.

HealthKit automatically extracts the custodian’s name from the CDA’s XML data.

## See Also

### Accessing the Document’s Data
- [var authorName: String](./authorname.md)
  The document’s author.
- [var documentData: Data?](./documentdata.md)
  The CDA document stored as XML data.
- [var patientName: String](./patientname.md)
  The patient’s name.
- [var title: String](./title.md)
  The document’s title.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkcdadocument/custodianname)*