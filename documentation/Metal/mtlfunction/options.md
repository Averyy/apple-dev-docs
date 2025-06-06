# options

**Framework**: Metal  
**Kind**: property  
**Required**: Yes

The options that Metal used to compile this function.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var options: MTLFunctionOptions { get }
```

## See Also

- [var device: any MTLDevice](mtlfunction/device.md)
  The device object that created the shader function.
- [var label: String?](mtlfunction/label.md)
  A string that identifies the shader function.
- [var functionType: MTLFunctionType](mtlfunction/functiontype.md)
  The shader function’s type.
- [var name: String](mtlfunction/name.md)
  The function’s name.
- [enum MTLFunctionType](mtlfunctiontype.md)
  The type of a top-level Metal Shading Language (MSL) function.
- [struct MTLFunctionOptions](mtlfunctionoptions.md)
  Options that define how Metal creates the function object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlfunction/options)*