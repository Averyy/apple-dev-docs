# exportData(with:to:destinationDataType:offset:rowStrides:)

**Framework**: Metal Performance Shaders  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func exportData(with cmdBuf: any MTLCommandBuffer, to buffer: any MTLBuffer, destinationDataType: MPSDataType, offset: Int, rowStrides: UnsafeMutablePointer<Int>?)
```

```objc
- (void) exportDataWithCommandBuffer:(id<MTLCommandBuffer>) cmdBuf toBuffer:(id<MTLBuffer>) buffer destinationDataType:(MPSDataType) destinationDataType offset:(NSUInteger) offset rowStrides:(NSInteger *) rowStrides;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsndarray/exportdata(with:to:destinationdatatype:offset:rowstrides:))*