# outputImage

**Framework**: Core Image  
**Kind**: property

Returns a [`CIImage`](ciimage.md) object that encapsulates the operations configured in the filter.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
var outputImage: CIImage? { get }
```

## See Also

- [var name: String](cifilter-swift.class/name.md)
  A name associated with a filter.
- [var isEnabled: Bool](cifilter-swift.class/isenabled.md)
  A Boolean value that determines whether the filter is enabled. Animatable.
- [var attributes: [String : Any]](cifilter-swift.class/attributes.md)
  A dictionary of key-value pairs that describe the filter.
- [var inputKeys: [String]](cifilter-swift.class/inputkeys.md)
  The names of all input parameters to the filter.
- [var outputKeys: [String]](cifilter-swift.class/outputkeys.md)
  The names of all output parameters from the filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/outputimage)*