# maximumItemCount

**Framework**: CarPlay  
**Kind**: property  
**Role**: Type Property

The maximum number of items, across all sections, that the template can display.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
class var maximumItemCount: Int { get }
```

```objc
@property (class, nonatomic, readonly) NSUInteger maximumItemCount;
```

## Discussion

When building your content, use this value to determine the maximum number of items to create. A vehicle can provide a specific value for this property to accommodate any user interface limits. You can determine if vehicle-specific limits are in place using the [`limitedUserInterfaces`](../cpsessionconfiguration/limiteduserinterfaces.md) property of [`CPSessionConfiguration`](../cpsessionconfiguration.md). Even without vehicle-specific limits, different app types support different limits on the amount of information to display.

## See Also

### Getting the configuration limits
- [class var maximumSectionCount: Int](./maximumsectioncount.md)
  The maximum number of sections the template can display.
- [class var maximumGridButtonImageSize: CGSize](./maximumgridbuttonimagesize.md)
  The expected image size for any grid buttons you add to the header.
- [class var maximumHeaderGridButtonCount: Int](./maximumheadergridbuttoncount.md)
  The maximum number of grid buttons you can display in the header.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplisttemplate/maximumitemcount)*