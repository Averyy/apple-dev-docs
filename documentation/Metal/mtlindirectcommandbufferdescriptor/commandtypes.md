# commandTypes

**Framework**: Metal  
**Kind**: property

The set of command types that you can encode into the indirect command buffer.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+

## Declaration

```swift
var commandTypes: MTLIndirectCommandType { get set }
```

#### Discussion

When you create the indirect command buffer, Metal allocates memory for each command it can hold. It needs to allocate enough memory to hold any command that you might later encode. To save space, specify only the command types you are going to encode in the indirect command buffer.

You can’t combine rendering and compute commands in the same indirect command buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlindirectcommandbufferdescriptor/commandtypes)*