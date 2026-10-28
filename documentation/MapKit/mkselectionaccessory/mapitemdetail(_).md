# mapItemDetail(_:)

**Framework**: MapKit  
**Kind**: method  
**Role**: Type Method

Detailed information about a place

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
class func mapItemDetail(_ presentationStyle: MKSelectionAccessory.MapItemDetailPresentationStyle) -> MKSelectionAccessory
```

```objc
+ (MKSelectionAccessory *) mapItemDetailWithPresentationStyle:(MKMapItemDetailSelectionAccessoryPresentationStyle *) presentationStyle;
```

## Discussion

Supported for [`MKMapFeatureAnnotation`](../mkmapfeatureannotation.md) and [`MKMapItemAnnotation`](../mkmapitemannotation.md).

## Parameters

- `presentationStyle`: The presentation style to use


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkselectionaccessory/mapitemdetail(_:))*