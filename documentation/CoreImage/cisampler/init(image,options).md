# init(image:options:)

**Framework**: Core Image  
**Kind**: init  
**Role**: Initializer

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

```objc
- (instancetype) initWithImage:(CIImage *) im options:(NSDictionary *) dict;
```

## Parameters

- `im`: The image to initialize the sampler with.
- `dict`: A dictionary that contains options specified as key-value pairs. See [Sampler Option Keys](../sampler-option-keys.md).

## See Also

### Initializing a Sampler
- [convenience init(image: CIImage)](./init%28image%29.md)
  Initializes a sampler with an image object.
### Related Documentation
- [- initWithImage:keysAndValues:](./initwithimage_keysandvalues_.md)
  Initializes the sampler with an image object using options specified as key-value pairs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cisampler/init(image:options:))*