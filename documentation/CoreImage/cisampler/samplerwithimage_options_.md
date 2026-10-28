# samplerWithImage:options:

**Framework**: Core Image  
**Kind**: method  
**Role**: Type Method

Creates and returns a sampler that references an image using options specified in a dictionary.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```objc
+ (instancetype) samplerWithImage:(CIImage *) im options:(NSDictionary *) dict;
```

## Return Value

A sampler that references the image specified by the `im` argument and uses the options specified in the dictionary.

## Parameters

- `im`: The image that you want the sampler to reference.
- `dict`: A dictionary that contains options specified as key-value pairs. See [Sampler Option Keys](../sampler-option-keys.md).

## See Also

### Creating a Sampler
- [+ samplerWithImage:](./samplerwithimage_.md)
  Creates and returns a sampler that references an image.
- [+ samplerWithImage:keysAndValues:](./samplerwithimage_keysandvalues_.md)
  Creates and returns a sampler that references an image using options specified as key-value pairs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cisampler/samplerwithimage:options:)*