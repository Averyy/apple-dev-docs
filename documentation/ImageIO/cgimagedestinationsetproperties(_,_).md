# CGImageDestinationSetProperties(_:_:)

**Framework**: Image I/O  
**Kind**: func  
**Role**: Function

Applies one or more properties to all images in an image destination.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func CGImageDestinationSetProperties(_ idst: CGImageDestination, _ properties: CFDictionary?)
```

```c
extern void CGImageDestinationSetProperties(CGImageDestinationRef idst, CFDictionaryRef properties);
```

## Parameters

- `idst`: The image destination to modify
- `properties`: A dictionary that contains the properties to apply. For a list of possible values, see [Image Properties](./image-properties.md) and doc:CGImageDestination/Configuring-the-Image-Behaviors.

## See Also

### Adding Metadata to the Image
- [func CGImageDestinationAddAuxiliaryDataInfo(CGImageDestination, CFString, CFDictionary)](./cgimagedestinationaddauxiliarydatainfo%28_,_,_%29.md)
  Sets the auxiliary data, such as mattes and depth information, that accompany the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageio/cgimagedestinationsetproperties(_:_:))*