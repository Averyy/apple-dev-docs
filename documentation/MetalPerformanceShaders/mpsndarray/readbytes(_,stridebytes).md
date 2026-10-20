# readBytes(_:strideBytes:)

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
func readBytes(_ buffer: UnsafeMutableRawPointer, strideBytes strideBytesPerDimension: UnsafeMutablePointer<Int>?)
```

```objc
- (void) readBytes:(void *) buffer strideBytes:(NSInteger *) strideBytesPerDimension;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsndarray/readbytes(_:stridebytes:))*