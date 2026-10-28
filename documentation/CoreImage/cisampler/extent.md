# extent

**Framework**: Core Image  
**Kind**: property  
**Role**: Instance Property

The rectangle that specifies the extent of the sampler

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var extent: CGRect { get }
```

```objc
@property (readonly) CGRect extent;
```

## Discussion

Extent is the rectangle that specifies the area outside which the wrap mode set for the sampler is invoked.

## See Also

### Getting Information About the Sampler Object
- [var definition: CIFilterShape](./definition.md)
  The domain of definition (DOD) of the sampler


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cisampler/extent)*