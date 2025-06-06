# init(ids:prefersPromotionalIcon:)

**Framework**: StoreKit  
**Kind**: init

Creates a view to load and merchandise a collection of products from the App Store using product identifiers.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
nonisolated
init(ids productIDs: some Collection<String>, prefersPromotionalIcon: Bool = false) where Icon == EmptyView, PlaceholderIcon == EmptyView
```

## Parameters

- `productIDs`: The product identifiers to load from the App Store.
- `prefersPromotionalIcon`: A Boolean value that indicates whether to use promotional images from the App Store, if they’re available. If this parameter is  , the system ignores promotional images.

## See Also

- [init(ids: some Collection<String>, prefersPromotionalIcon: Bool, icon: (Product) -> Icon)](storeview/init(ids:preferspromotionalicon:icon:).md)
  Creates a view to load a collection of products from the App Store using product identifiers, and merchandise them using a custom image.
- [init(ids: some Collection<String>, prefersPromotionalIcon: Bool, icon: (Product) -> Icon, placeholderIcon: () -> PlaceholderIcon)](storeview/init(ids:preferspromotionalicon:icon:placeholdericon:).md)
  Creates a view to load a collection of products from the App Store using product identifiers, and merchandise them using an image and a custom placeholder icon.
- [init(ids: some Collection<String>, icon: (Product, ProductIconPhase) -> Icon, placeholderIcon: () -> PlaceholderIcon)](storeview/init(ids:icon:placeholdericon:).md)
  Creates a view to load a collection of products from the App Store using product identifiers, and merchandise them using their promotional images and a custom placeholder icon.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/storeview/init(ids:preferspromotionalicon:))*