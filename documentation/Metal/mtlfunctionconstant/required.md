# required

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the function constant needs to be provided to specialize the function.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var required: Bool { get }
```

```objc
@property (readonly) BOOL required;
```

#### Discussion

This value is [`true`](../../Swift/true.md) if a constant value needs to be provided for the function constant. A function constant is optional only if it is referenced in a call to the built-in `is_function_constant_defined(name)` function.

Refer to the [Metal Shading Language Guide](https://developer.apple.com/library/archive/documentation/Metal/Reference/MetalShadingLanguageGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40014364) for more information.

## See Also

### Reading the function constant’s properties
- [var name: String](./name.md)
  The name of the function constant.
- [var type: MTLDataType](./type.md)
  The data type of the function constant.
- [var index: Int](./index.md)
  The index of the function constant.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlfunctionconstant/required)*