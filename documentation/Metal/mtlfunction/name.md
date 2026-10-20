# name

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The function’s name.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var name: String { get }
```

```objc
@property (readonly) NSString * name;
```

## See Also

### Identifying shader functions
- [var device: any MTLDevice](./device.md)
  The device object that created the shader function.
- [var label: String?](./label.md)
  A string that identifies the shader function.
- [var functionType: MTLFunctionType](./functiontype.md)
  The shader function’s type.
- [enum MTLFunctionType](../mtlfunctiontype.md)
  The type of a top-level Metal Shading Language (MSL) function.
- [var options: MTLFunctionOptions](./options.md)
  The options that Metal used to compile this function.
- [struct MTLFunctionOptions](../mtlfunctionoptions.md)
  Options that define how Metal compiles a GPU function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlfunction/name)*