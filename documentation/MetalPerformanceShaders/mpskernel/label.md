# label

**Framework**: Metal Performance Shaders  
**Kind**: property  
**Role**: Instance Property

The string that identifies the kernel.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var label: String? { get set }
```

```objc
@property (atomic, copy, nullable) NSString * label;
```

## See Also

### Properties
- [var options: MPSKernelOptions](./options.md)
  The set of options used to run the kernel.
- [struct MPSKernelOptions](../mpskerneloptions.md)
  The options used when creating a kernel.
- [var device: any MTLDevice](./device.md)
  The device on which the kernel will be used.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpskernel/label)*