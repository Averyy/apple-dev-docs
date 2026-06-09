# providerDataTypeIdentifiers

**Framework**: Core Spotlight  
**Kind**: property

An array of type identifiers that correspond to data types your delegate object can provide.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- visionOS 1.0+

## Declaration

```swift
var providerDataTypeIdentifiers: [String]? { get set }
```

#### Discussion

Use this property to specify the content types that your app or Core Spotlight delegate app extension can provide to satisfy a drag-and-drop request involving a searchable item. When a drag-and-drop action occurs, the app receiving the data selects the type it wants from the identifiers you provide. To deliver the data for one of the types in this property, the system calls the [`data(for:itemIdentifier:typeIdentifier:)`](cssearchableindexdelegate/data(for:itemidentifier:typeidentifier:).md) method of your delegate object.

Arrange the types in this property in order from highest to lowest fidelity.

## See Also

- [var providerFileTypeIdentifiers: [String]?](cssearchableitemattributeset/providerfiletypeidentifiers.md)
  An array of type identifiers that correspond to file types your delegate object can provide.
- [var providerInPlaceFileTypeIdentifiers: [String]?](cssearchableitemattributeset/providerinplacefiletypeidentifiers.md)
  An array of type identifiers that correspond to in-place file types your delegate object can provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/providerdatatypeidentifiers)*