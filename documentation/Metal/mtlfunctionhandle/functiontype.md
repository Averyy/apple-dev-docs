# functionType

**Framework**: Metal  
**Kind**: property  
**Required**: Yes

The shader function’s type.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var functionType: MTLFunctionType { get }
```

#### Discussion

A function’s type determines what kind of pipeline state objects you can create from it.

## See Also

- [var device: any MTLDevice](mtlfunctionhandle/device.md)
  The device object that created the shader function.
- [var name: String](mtlfunctionhandle/name.md)
  The function’s name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlfunctionhandle/functiontype)*