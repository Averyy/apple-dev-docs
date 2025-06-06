# isActive

**Framework**: Metal  
**Kind**: property

A Boolean that indicates whether the compiled function uses the argument.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
var isActive: Bool { get }
```

#### Discussion

When you create the [`MTLFunction`](mtlfunction.md) object, Metal statically determines whether the function uses the argument. If [`true`](https://developer.apple.com/documentation/swift/true), you must provide a value for this argument when you encode a command that calls this function. If [`false`](https://developer.apple.com/documentation/swift/false), the function doesn’t use the argument, and you can ignore it.

## See Also

- [var name: String](mtlargument/name.md)
  The name of the argument.
- [var index: Int](mtlargument/index.md)
  The index in the argument table that corresponds to the function argument.
- [var type: MTLArgumentType](mtlargument/type.md)
  The argument’s resource type.
- [var access: MTLBindingAccess](mtlargument/access.md)
  The argument’s read and/or write access.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlargument/isactive)*