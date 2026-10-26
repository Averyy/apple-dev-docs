# initWithImage:keysAndValues:

**Framework**: Core Image  
**Kind**: method  
**Role**: Instance Method

Initializes the sampler with an image object using options specified as key-value pairs.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```objc
- (instancetype) initWithImage:(CIImage *) im keysAndValues:(id) key0;
```

## Parameters

- `im`: The image object to initialize the sampler with.
- `key0`: A list of key-value pairs that represent options.  Each key needs to be followed by that appropriate value. You can supply one or more key-value pairs. Use `nil` to specify the end of the key-value options. See [Sampler Option Keys](../sampler-option-keys.md).

## See Also

### Initializing a Sampler
- [convenience init(image: CIImage)](./init%28image%29.md)
  Initializes a sampler with an image object.
- [init(image: CIImage, options: [AnyHashable : Any]?)](./init%28image,options%29.md)
  Initializes the sampler with an image object using options specified in a dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cisampler/initwithimage:keysandvalues:)*