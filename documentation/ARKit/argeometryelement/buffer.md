# buffer

**Framework**: ARKit  
**Kind**: property  
**Role**: Instance Property

A Metal buffer containing primitive data.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+

## Declaration

```swift
var buffer: any MTLBuffer { get }
```

```objc
@property (nonatomic, strong, readonly) id<MTLBuffer> buffer;
```

## See Also

### Accessing Index Data
- [subscript(Int) -> [Int32]](./subscript%28_%29.md)
  Provides an array of vertex indices that respresents the geometric primitive at the subscripted index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/argeometryelement/buffer)*