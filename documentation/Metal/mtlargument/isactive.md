# isActive

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

A Boolean that indicates whether the compiled function uses the argument.

**Availability**:
- iOS 8.0+ - Deprecated in 16.0
- iPadOS 8.0+ - Deprecated in 16.0
- Mac Catalyst 13.1+ - Deprecated in 16.0
- macOS 10.11+ - Deprecated in 13.0
- tvOS - Deprecated in 16.0
- visionOS 1.0+ - Deprecated in 1.0

## Declaration

```swift
var isActive: Bool { get }
```

```objc
@property (readonly, getter=isActive) BOOL active;
```

#### Discussion

When you create the [`MTLFunction`](../mtlfunction.md) object, Metal statically determines whether the function uses the argument. If [`true`](../../Swift/true.md), you need to provide a value for this argument when you encode a command that calls this function. If [`false`](../../Swift/false.md), the function doesn’t use the argument, and you can ignore it.

## See Also

### Describing the argument
- [var name: String](./name.md)
  The name of the argument.
- [var index: Int](./index.md)
  The index in the argument table that corresponds to the function argument.
- [var type: MTLArgumentType](./type.md)
  The argument’s resource type.
- [var access: MTLBindingAccess](./access.md)
  The argument’s read and/or write access.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlargument/isactive)*