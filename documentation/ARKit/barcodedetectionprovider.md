# BarcodeDetectionProvider

**Framework**: ARKit  
**Kind**: class

An object that provides the real-time position of barcodes the framework detects in a person’s environment.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
final class BarcodeDetectionProvider
```

#### Overview

Use this provider to receive updates about barcodes that ARKit detect in a person’s surroundings, This provider returns the results in the form of an asynchronous sequence of [`BarcodeAnchor`](barcodeanchor.md) structures. Your app needs to include the [`Spatial barcode and QR code scanning`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.arkit.barcode-detection.allow) entitlement to use this capability; otherwise, it has no effect.

## Topics

### Creating a barcode detection provider
- [init(symbologies: [BarcodeAnchor.Symbology])](barcodedetectionprovider/init(symbologies:).md)
  Creates a barcode detection provider that looks for the specified symbologies.
### Inspecting a barcode detection provider
- [var anchorUpdates: AnchorUpdateSequence<BarcodeAnchor>](barcodedetectionprovider/anchorupdates.md)
  An asynchronous sequence of anchor updates that describe the anchors in a person’s surroundings.
- [var description: String](barcodedetectionprovider/description.md)
  A textual representation of this barcode detection provider.
- [var state: DataProviderState](barcodedetectionprovider/state.md)
  The state of a barcode detection provider.
### Type properties
- [static var isSupported: Bool](barcodedetectionprovider/issupported.md)
  A Boolean value that determines whether a device supports the barcode detection provider.
- [static var requiredAuthorizations: [ARKitSession.AuthorizationType]](barcodedetectionprovider/requiredauthorizations.md)
  The authorization types you need to use the barcode detection provider.

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [DataProvider](dataprovider.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct BarcodeAnchor](barcodeanchor.md)
  A barcode’s position in a person’s surroundings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/barcodedetectionprovider)*