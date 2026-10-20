# init(device:transpose:rows:columns:alpha:beta:)

**Framework**: Metal Performance Shaders  
**Kind**: init  
**Role**: Initializer

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
init(device: any MTLDevice, transpose: Bool, rows: Int, columns: Int, alpha: Double, beta: Double)
```

```objc
- (instancetype) initWithDevice:(id<MTLDevice>) device transpose:(BOOL) transpose rows:(NSUInteger) rows columns:(NSUInteger) columns alpha:(double) alpha beta:(double) beta;
```

## See Also

### Initializers
- [init(device: any MTLDevice, rows: Int, columns: Int)](./init%28device,rows,columns%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsmatrixvectormultiplication/init(device:transpose:rows:columns:alpha:beta:))*