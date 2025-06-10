# visibleItemsInvalidationHandler

**Framework**: UIKit  
**Kind**: property

A closure called before each layout cycle to allow modification of the items in the section immediately before they’re displayed.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var visibleItemsInvalidationHandler: NSCollectionLayoutSectionVisibleItemsInvalidationHandler? { get set }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nscollectionlayoutsection/visibleitemsinvalidationhandler)*