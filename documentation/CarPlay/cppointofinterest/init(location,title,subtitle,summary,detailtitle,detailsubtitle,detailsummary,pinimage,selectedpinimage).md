# init(location:title:subtitle:summary:detailTitle:detailSubtitle:detailSummary:pinImage:selectedPinImage:)

**Framework**: CarPlay  
**Kind**: init  
**Role**: Initializer

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
init(location: MKMapItem, title: String, subtitle: String?, summary: String?, detailTitle: String?, detailSubtitle: String?, detailSummary: String?, pinImage: UIImage?, selectedPinImage: UIImage?)
```

```objc
- (instancetype) initWithLocation:(MKMapItem *) location title:(NSString *) title subtitle:(NSString *) subtitle summary:(NSString *) summary detailTitle:(NSString *) detailTitle detailSubtitle:(NSString *) detailSubtitle detailSummary:(NSString *) detailSummary pinImage:(UIImage *) pinImage selectedPinImage:(UIImage *) selectedPinImage;
```

## See Also

### Creating a point of interest
- [convenience init(location: MKMapItem, title: String, subtitle: String?, summary: String?, detailTitle: String?, detailSubtitle: String?, detailSummary: String?, pinImage: UIImage?)](./init%28location,title,subtitle,summary,detailtitle,detailsubtitle,detailsummary,pinimage%29.md)
  Creates a point of interest for a specific location.
- [init?(coder: NSCoder)](./init%28coder%29.md)
- [class var pinImageSize: CGSize](./pinimagesize.md)
- [class var selectedPinImageSize: CGSize](./selectedpinimagesize.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cppointofinterest/init(location:title:subtitle:summary:detailtitle:detailsubtitle:detailsummary:pinimage:selectedpinimage:))*