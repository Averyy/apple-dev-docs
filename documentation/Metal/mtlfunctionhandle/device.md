# device

**Framework**: Metal  
**Kind**: property  
**Required**: Yes

The device object that created the shader function.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var device: any MTLDevice { get }
```

#### Discussion

You can only use the function handle with this [`MTLDevice`](mtldevice.md).

## See Also

- [Metal Shading Language Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Metal/Reference/MetalShadingLanguageGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40014364)
- [Metal Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Miscellaneous/Conceptual/MetalProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40014221)
- [var functionType: MTLFunctionType](mtlfunctionhandle/functiontype.md)
  The shader function’s type.
- [var name: String](mtlfunctionhandle/name.md)
  The function’s name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlfunctionhandle/device)*