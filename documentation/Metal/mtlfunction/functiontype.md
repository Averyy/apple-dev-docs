# functionType

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The shader function’s type.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var functionType: MTLFunctionType { get }
```

```objc
@property (readonly) MTLFunctionType functionType;
```

#### Discussion

A function’s type determines what kind of pipeline state objects you can create from it and whether you can use it as a callable function in a function table.

## See Also

### Identifying shader functions
- [var device: any MTLDevice](./device.md)
  The device object that created the shader function.
- [var label: String?](./label.md)
  A string that identifies the shader function.
- [var name: String](./name.md)
  The function’s name.
- [enum MTLFunctionType](../mtlfunctiontype.md)
  The type of a top-level Metal Shading Language (MSL) function.
- [var options: MTLFunctionOptions](./options.md)
  The options that Metal used to compile this function.
- [struct MTLFunctionOptions](../mtlfunctionoptions.md)
  Options that define how Metal compiles a GPU function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlfunction/functiontype)*