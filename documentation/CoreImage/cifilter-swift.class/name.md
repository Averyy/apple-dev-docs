# name

**Framework**: Core Image  
**Kind**: property  
**Role**: Instance Property

A name associated with a filter.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var name: String { get set }
```

```objc
@property (nonatomic, copy) NSString * name;
```

## Discussion

You use a filter’s name to construct key paths to its attributes when the filter is attached to a Core Animation layer. For example, if a [`CALayer`](../../QuartzCore/calayer.md) object has an attached [`CIFilter`](../cifilter-swift.class.md) instance whose name is `myExposureFilter`, you can refer to attributes of the filter using a key path such as `filters.myExposureFilter.inputEV`. Layer animations may also access filter attributes via these key paths.

Core Animation can animate this property on a layer.

The default value for this property is `nil`.

## See Also

### Getting filter parameters and attributes
- [var isEnabled: Bool](./isenabled.md)
  A Boolean value that determines whether the filter is enabled. Animatable.
- [var attributes: [String : Any]](./attributes.md)
  A dictionary of key-value pairs that describe the filter.
- [var inputKeys: [String]](./inputkeys.md)
  The names of all input parameters to the filter.
- [var outputKeys: [String]](./outputkeys.md)
  The names of all output parameters from the filter.
- [var outputImage: CIImage?](./outputimage.md)
  Returns a [`CIImage`](../ciimage.md) object that encapsulates the operations configured in the filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/name)*