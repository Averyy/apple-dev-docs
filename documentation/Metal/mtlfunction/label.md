# label

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property  
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

```objc
@property (atomic, copy, nullable) NSString * label;
```

## Discussion

Object and command labels are useful identifiers at runtime or when profiling and debugging your app using any Metal tool. See [Naming resources and commands](../../Xcode/naming-resources-and-commands.md).

## See Also

### Identifying shader functions
- [var device: any MTLDevice](./device.md)
  The device object that created the shader function.
- [var functionType: MTLFunctionType](./functiontype.md)
  The shader function’s type.
- [var name: String](./name.md)
  The function’s name.
- [enum MTLFunctionType](../mtlfunctiontype.md)
  The type of a top-level Metal Shading Language (MSL) function.
- [var options: MTLFunctionOptions](./options.md)
  The options that Metal used to compile this function.
- [struct MTLFunctionOptions](../mtlfunctionoptions.md)
  Options that define how Metal compiles a GPU function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlfunction/label)*