# document

**Framework**: HealthKit  
**Kind**: property

The CDA document.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var document: HKCDADocument? { get }
```

#### Discussion

If the user is authorized to access the document’s data, this property contains an [`HKCDADocument`](hkcdadocument.md) object representing that data. Otherwise, it is set to `nil`.

The user is asked to authorize each CDA document the first time that document is returned by an [`HKDocumentQuery`](hkdocumentquery.md) query. The user can change the access permissions in the Health app.

For samples returned by an [`HKSampleQuery`](hksamplequery.md) or an [`HKAnchoredObjectQuery`](hkanchoredobjectquery.md), this property is always set to `nil`. To access the document’s data from these samples, create a [`HKDocumentQuery`](hkdocumentquery.md) query for the sample’s UUID.

## See Also

- [class HKCDADocument](hkcdadocument.md)
  An object representing a Clinical Document Architecture (CDA) document in HealthKit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkcdadocumentsample/document)*