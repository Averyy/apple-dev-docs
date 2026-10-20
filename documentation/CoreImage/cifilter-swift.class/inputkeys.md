# inputKeys

**Framework**: Core Image  
**Kind**: property  
**Role**: Instance Property

The names of all input parameters to the filter.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var inputKeys: [String] { get }
```

```objc
@property (nonatomic, readonly) NSArray<NSString *> * inputKeys;
```

## See Also

### Getting filter parameters and attributes
- [var name: String](./name.md)
  A name associated with a filter.
- [var isEnabled: Bool](./isenabled.md)
  A Boolean value that determines whether the filter is enabled. Animatable.
- [var attributes: [String : Any]](./attributes.md)
  A dictionary of key-value pairs that describe the filter.
- [var outputKeys: [String]](./outputkeys.md)
  The names of all output parameters from the filter.
- [var outputImage: CIImage?](./outputimage.md)
  Returns a [`CIImage`](../ciimage.md) object that encapsulates the operations configured in the filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/inputkeys)*