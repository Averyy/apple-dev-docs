# CFMachPortContext

**Framework**: Core Foundation  
**Kind**: struct  
**Role**: Structure

A structure that contains program-defined data and callbacks with which you can configure a CFMachPort object’s behavior.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
struct CFMachPortContext
```

```c
typedef struct { ... } CFMachPortContext;
```

## Topics

### Initializers
- [init()](./cfmachportcontext/init%28%29.md)
- [init(version: CFIndex, info: UnsafeMutableRawPointer!, retain: ((UnsafeRawPointer?) -> UnsafeRawPointer?)!, release: ((UnsafeRawPointer?) -> Void)!, copyDescription: ((UnsafeRawPointer?) -> Unmanaged<CFString>?)!)](./cfmachportcontext/init%28version,info,retain,release,copydescription%29.md)
### Instance Properties
- [var copyDescription: ((UnsafeRawPointer?) -> Unmanaged<CFString>?)!](./cfmachportcontext/copydescription.md)
  A copy description callback for your program-defined `info` pointer. Can be `NULL`.
- [var info: UnsafeMutableRawPointer!](./cfmachportcontext/info.md)
  An arbitrary pointer to program-defined data, which can be associated with the CFMachPort object at creation time. This pointer is passed to all the callbacks defined in the context.
- [var release: ((UnsafeRawPointer?) -> Void)!](./cfmachportcontext/release.md)
  A release callback for your program-defined `info` pointer. Can be `NULL`.
- [var retain: ((UnsafeRawPointer?) -> UnsafeRawPointer?)!](./cfmachportcontext/retain.md)
  A retain callback for your program-defined `info` pointer. Can be `NULL`.
- [var version: CFIndex](./cfmachportcontext/version.md)
  Version number of the structure. Must be `0`.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfmachportcontext)*