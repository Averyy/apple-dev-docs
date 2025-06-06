# label

**Framework**: Metal  
**Kind**: property  
**Required**: Yes

A string that identifies the shader function.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var label: String? { get set }
```

#### Discussion

Object and command labels are useful identifiers at runtime or when profiling and debugging your app using any Metal tool. See `Enhancing Frame Capture by Using Labels`.

## See Also

- [var device: any MTLDevice](mtlfunction/device.md)
  The device object that created the shader function.
- [var functionType: MTLFunctionType](mtlfunction/functiontype.md)
  The shader function’s type.
- [var name: String](mtlfunction/name.md)
  The function’s name.
- [enum MTLFunctionType](mtlfunctiontype.md)
  The type of a top-level Metal Shading Language (MSL) function.
- [var options: MTLFunctionOptions](mtlfunction/options.md)
  The options that Metal used to compile this function.
- [struct MTLFunctionOptions](mtlfunctionoptions.md)
  Options that define how Metal creates the function object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlfunction/label)*