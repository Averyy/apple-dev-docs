# CGImageDestinationSetProperties(_:_:)

**Framework**: Image I/O  
**Kind**: func

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

## Parameters

- `idst`: The image destination to modify
- `properties`: A dictionary that contains the properties to apply. For a list of possible values, see   and  .

## See Also

- [func CGImageDestinationAddAuxiliaryDataInfo(CGImageDestination, CFString, CFDictionary)](cgimagedestinationaddauxiliarydatainfo(_:_:_:).md)
  Sets the auxiliary data, such as mattes and depth information, that accompany the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageio/cgimagedestinationsetproperties(_:_:))*