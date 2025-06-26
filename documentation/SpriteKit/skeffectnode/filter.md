# filter

**Framework**: SpriteKit  
**Kind**: property

The Core Image filter to apply.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
var filter: CIFilter? { get set }
```

#### Discussion

The Core Image filter must have a single `inputImage` parameter and produce a single `outputImage` parameter. The default value is `nil`. If the value is `nil` and the effect node is enabled, no filtering takes place. However, its children are still rendered in a separate pass and blended to the parent’s framebuffer.

If you wish to use a Core Image filter that doesn’t have an `inputImage` parameter, such as a sunbeams generator, you can subclass [`CIFilter`](https://developer.apple.com/documentation/CoreImage/CIFilter-swift.class) and add an `inputImage` property. The input image’s extent can be used to define properties such as radius on the filter. The following code creates a filter based on [`CISunbeamsGenerator`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/GraphicsImaging/Reference/CoreImageFilterReference/index.html#//apple_ref/doc/filter/ci/CISunbeamsGenerator) which can be used as an effect node’s filter:

```objc
class StarGenerator: CIFilter {    
    var inputImage: CIImage?        
    override var outputImage: CIImage? {        
        guard let inputImage = inputImage else {            
            return nil        
        }                
        let extent = inputImage.extent                
        let center = CIVector(x: extent.midX, y: extent.midY)                
        let starShineGenerator = CIFilter(            
            name: "CISunbeamsGenerator",            
            withInputParameters: [                
                "inputMaxStriationRadius": 2,                
                "inputSunRadius": extent.midX / 2,                
            kCIInputCenterKey: center])                
        return starShineGenerator!.outputImage?.cropping(to: extent)    
    }
}
```

## See Also

- [Applying Special Effects to a Node’s Children](applying-special-effects-to-a-node-s-children.md)
  Apply the Core Image suite of filters to child nodes of an effect node.
- [var shouldEnableEffects: Bool](skeffectnode/shouldenableeffects.md)
  A Boolean value that determines whether the effect node applies the filter to its children as they are drawn.
- [var shouldCenterFilter: Bool](skeffectnode/shouldcenterfilter.md)
  A Boolean value that determines whether the effect node automatically sets the filter’s image center.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skeffectnode/filter)*