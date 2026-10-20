# sheet(presentedFrom:)

**Framework**: MapKit  
**Kind**: method  
**Role**: Type Method

Show map item detail by presenting a sheet.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

*iOS, iPadOS, Mac Catalyst, visionOS*

```swift
class func sheet(presentedFrom viewController: UIViewController) -> MKSelectionAccessory.MapItemDetailPresentationStyle
```

*macOS*

```swift
class func sheet(presentedFrom viewController: NSViewController) -> MKSelectionAccessory.MapItemDetailPresentationStyle
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```objc
+ (MKMapItemDetailSelectionAccessoryPresentationStyle *) sheetPresentedFromViewController:(UIViewController *) viewController;
```

*macOS*

```objc
+ (MKMapItemDetailSelectionAccessoryPresentationStyle *) sheetPresentedFromViewController:(NSViewController *) viewController;
```

## Parameters

- `viewController`: The view controller that will present the sheet.

## See Also

### Creating a presentation style
- [static func automatic(presentationViewController: UIViewController?) -> MKSelectionAccessory.MapItemDetailPresentationStyle](./automatic%28presentationviewcontroller%29-648ee.md)
  An appropriate presentation style will be chosen automatically.
- [static func automatic(presentationViewController: NSViewController?) -> MKSelectionAccessory.MapItemDetailPresentationStyle](./automatic%28presentationviewcontroller%29-9t9vt.md)
  An appropriate presentation style will be chosen automatically.
- [class var callout: MKSelectionAccessory.MapItemDetailPresentationStyle](./callout.md)
  Show map item detail as an annotation callout on the map.
- [static func callout(MKSelectionAccessory.MapItemDetailPresentationStyle.CalloutStyle) -> MKSelectionAccessory.MapItemDetailPresentationStyle](./callout%28_%29.md)
  Show map item detail as an annotation callout on the map
- [class var openInMaps: MKSelectionAccessory.MapItemDetailPresentationStyle](./openinmaps.md)
  Display a small “Open in Apple Maps” link.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkselectionaccessory/mapitemdetailpresentationstyle/sheet(presentedfrom:))*