# init(pdfURL:authors:id:)

**Framework**: Assignables  
**Kind**: init

Initializes a new assessment document that is based on the PDF located at the provided URL. If the file located at the URL provided cannot be accessed, this initializer throws.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- visionOS ?+
- Unknown ?+ - Deprecated

## Declaration

```swift
init(pdfURL: URL, authors: [some UserIdentity], id: String? = nil) throws
```

## Parameters

- `pdfURL`: A URL to the PDF document that   is the basis of this assessment document.
- `authors`: The user identities of contributors to this document. Treated as a set.
- `id`: An optional ID to use for this document.   if one is not provided, a random UUID string will be used.

## See Also

- [init(pdfURL: URL, id: String?) throws](assignabledocument/init(pdfurl:id:).md)
  Initializes a new assessment document that is based on the PDF located at the provided URL. If the file located at the URL provided cannot be accessed, this initializer throws.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/assignabledocument/init(pdfurl:authors:id:))*