# ProductIconPhase

**Framework**: StoreKit  
**Kind**: enum

The current phase of the asynchronous loading operation of a product’s promotional image.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
enum ProductIconPhase
```

#### Overview

When you create a [`ProductIconPhase`](producticonphase.md) instance with an initializer such as [`init(ids:icon:placeholderIcon:)`](storeview/init(ids:icon:placeholdericon:).md), you define the appearance of the view’s icon, or image, using a content closure. SwiftUI calls the closure at different stages of the promotional image’s load operation with a phase value that indicates the current state.

Use the phase to decide what to draw. For example, you can draw a placeholder image during the loading phase, a view that indicates an error, a default image, or the loaded promotional image if it exists:

```swift
StoreView(products: [
     product1,
     product2,
     // Additional products, as needed.
 ]) { product, phase in
     switch phase {
     case .loading: MyPlaceholder()
     case .failure(let error): MyErrorView(error)
     case .unavailable: MyDefaultIcon()
     case .success(let promotedIcon): promotedIcon
     }
 }
```

You set up promotional images for in-app purchases in App Store Connect. For more information, see [`Promote in-app purchases`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/configure-in-app-purchase-settings/promote-in-app-purchases).

## Topics

### Getting the promotional image’s load phases
- [ProductIconPhase.loading](producticonphase/loading.md)
  The promotional image is in the process of loading.
- [ProductIconPhase.success(_:)](producticonphase/success(_:).md)
  The promotional image successfully loaded.
- [ProductIconPhase.unavailable](producticonphase/unavailable.md)
  The promotional image isn’t available for download.
- [ProductIconPhase.failure(_:)](producticonphase/failure(_:).md)
  The promotional image failed to load, with an error.
### Getting the promotional image
- [var promotionalIcon: Image?](producticonphase/promotionalicon.md)
  The promotional image, if the loading task is successful.
### Getting the error
- [var error: (any Error)?](producticonphase/error.md)
  The error value that indicates the reason a promotional image failed to load.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/producticonphase)*