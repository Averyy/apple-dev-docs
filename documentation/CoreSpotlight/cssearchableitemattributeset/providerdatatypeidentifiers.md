# providerDataTypeIdentifiers

**Framework**: Core Spotlight  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (copy, nullable) NSArray<NSString *> * providerDataTypeIdentifiers;
```

## Discussion

Use this property to specify the content types that your app or Core Spotlight delegate app extension can provide to satisfy a drag-and-drop request involving a searchable item. When a drag-and-drop action occurs, the app receiving the data selects the type it wants from the identifiers you provide. To deliver the data for one of the types in this property, the system calls the [`data(for:itemIdentifier:typeIdentifier:)`](../cssearchableindexdelegate/data%28for,itemidentifier,typeidentifier%29.md) method of your delegate object.

Arrange the types in this property in order from highest to lowest fidelity.

## See Also

### Providing item representations
- [var providerFileTypeIdentifiers: [String]?](./providerfiletypeidentifiers.md)
  An array of type identifiers that correspond to file types your delegate object can provide.
- [var providerInPlaceFileTypeIdentifiers: [String]?](./providerinplacefiletypeidentifiers.md)
  An array of type identifiers that correspond to in-place file types your delegate object can provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/providerdatatypeidentifiers)*