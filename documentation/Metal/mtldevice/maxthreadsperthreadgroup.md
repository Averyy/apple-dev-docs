# maxThreadsPerThreadgroup

**Framework**: Metal  
**Kind**: property  
**Required**: Yes

The maximum number of threads along each dimension of a threadgroup.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var maxThreadsPerThreadgroup: MTLSize { get }
```

#### Discussion

This size isn’t guaranteed for all shaders. The number of trival shaders supported at once on device determines this value. For more accurate information on the allowable maximum threads per threadgroup in an individual pass, inspect your associated pipeline state.

For more information on the specific threadgroup limits of each GPU family, see the Metal feature set tables:

- [`Metal feature set tables (PDF)`](https://developer.apple.comhttps://developer.apple.com/metal/Metal-Feature-Set-Tables.pdf)
- [`Metal feature set tables (Numbers)`](https://developer.apple.comhttps://developer.apple.com/metal/metal-feature-set-tables.zip)

## See Also

- [var maxThreadgroupMemoryLength: Int](mtldevice/maxthreadgroupmemorylength.md)
  The maximum threadgroup memory available to a compute kernel, in bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldevice/maxthreadsperthreadgroup)*