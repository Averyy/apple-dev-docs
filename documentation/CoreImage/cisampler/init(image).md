# init(image:)

**Framework**: Core Image  
**Kind**: init  
**Role**: Initializer

Initializes a sampler with an image object.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
convenience init(image im: CIImage)
```

```objc
- (instancetype) initWithImage:(CIImage *) im;
```

## Parameters

- `im`: The image object to initialize the sampler with.

## See Also

### Initializing a Sampler
- [init(image: CIImage, options: [AnyHashable : Any]?)](./init%28image,options%29.md)
  Initializes the sampler with an image object using options specified in a dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cisampler/init(image:))*