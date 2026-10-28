# title

**Framework**: HealthKit  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (copy, readonly) NSString * title;
```

## Discussion

HealthKit automatically extracts the document’s title from the CDA’s XML data.

## See Also

### Accessing the Document’s Data
- [var authorName: String](./authorname.md)
  The document’s author.
- [var custodianName: String](./custodianname.md)
  The name of the organization responsible for the document.
- [var documentData: Data?](./documentdata.md)
  The CDA document stored as XML data.
- [var patientName: String](./patientname.md)
  The patient’s name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkcdadocument/title)*