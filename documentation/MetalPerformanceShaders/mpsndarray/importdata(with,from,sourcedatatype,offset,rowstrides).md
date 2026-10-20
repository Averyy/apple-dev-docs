# importData(with:from:sourceDataType:offset:rowStrides:)

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
func importData(with cmdBuf: any MTLCommandBuffer, from buffer: any MTLBuffer, sourceDataType: MPSDataType, offset: Int, rowStrides: UnsafeMutablePointer<Int>?)
```

```objc
- (void) importDataWithCommandBuffer:(id<MTLCommandBuffer>) cmdBuf fromBuffer:(id<MTLBuffer>) buffer sourceDataType:(MPSDataType) sourceDataType offset:(NSUInteger) offset rowStrides:(NSInteger *) rowStrides;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsndarray/importdata(with:from:sourcedatatype:offset:rowstrides:))*