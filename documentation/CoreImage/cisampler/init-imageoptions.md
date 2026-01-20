# init(image:options:)

**Framework**: Core Image  
**Kind**: init

Initializes the sampler with an image object using options specified in a dictionary.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
init(image im: CIImage, options dict: [AnyHashable : Any]? = nil)
```

## Parameters

- `im`: The image to initialize the sampler with.
- `dict`: A dictionary that contains options specified as key-value pairs. See  .

## See Also

- [convenience init(image: CIImage)](cisampler/init(image:).md)
  Initializes a sampler with an image object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cisampler/init(image:options:))*