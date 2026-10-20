# label

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

A string that identifies the sampler.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var label: String? { get }
```

```objc
@property (readonly, nullable) NSString * label;
```

#### Discussion

Object and command labels are useful identifiers at runtime or when profiling and debugging your app using any Metal tool. See [Naming resources and commands](../../Xcode/naming-resources-and-commands.md).

## See Also

### Identifying the sampler
- [var device: any MTLDevice](./device.md)
  The device object that created the sampler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlsamplerstate/label)*