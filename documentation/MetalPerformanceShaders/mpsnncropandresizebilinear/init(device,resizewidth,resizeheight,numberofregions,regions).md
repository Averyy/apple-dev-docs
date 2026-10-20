# init(device:resizeWidth:resizeHeight:numberOfRegions:regions:)

**Framework**: Metal Performance Shaders  
**Kind**: init  
**Role**: Initializer

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.0+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+

## Declaration

```swift
init(device: any MTLDevice, resizeWidth: Int, resizeHeight: Int, numberOfRegions: Int, regions: UnsafePointer<MPSRegion>)
```

```objc
- (instancetype) initWithDevice:(id<MTLDevice>) device resizeWidth:(NSUInteger) resizeWidth resizeHeight:(NSUInteger) resizeHeight numberOfRegions:(NSUInteger) numberOfRegions regions:(const MPSRegion *) regions;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsnncropandresizebilinear/init(device:resizewidth:resizeheight:numberofregions:regions:))*