# options

**Framework**: Metal Performance Shaders  
**Kind**: property  
**Role**: Instance Property

The set of options used to run the kernel.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var options: MPSKernelOptions { get set }
```

```objc
@property (nonatomic, readwrite) MPSKernelOptions options;
```

## See Also

### Properties
- [struct MPSKernelOptions](../mpskerneloptions.md)
  The options used when creating a kernel.
- [var device: any MTLDevice](./device.md)
  The device on which the kernel will be used.
- [var label: String?](./label.md)
  The string that identifies the kernel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpskernel/options)*