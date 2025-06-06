# CFAllocatorGetContext(_:_:)

**Framework**: Core Foundation  
**Kind**: func

Obtains the context of the specified allocator or of the default allocator.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
func CFAllocatorGetContext(_ allocator: CFAllocator!, _ context: UnsafeMutablePointer<CFAllocatorContext>!)
```

#### Discussion

An allocator’s context, a structure of type `CFAllocatorContext`, holds pointers to various function callbacks (particularly those that allocate, reallocate, and deallocate memory for an object). The context also contains a version number and the `info` field for program-defined data. To obtain the value of the `info` field you usually first have to get an allocator’s context.

## Parameters

- `allocator`: The allocator to examine. Pass   to obtain the context of the default allocator.
- `context`: On return, contains the context of  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfallocatorgetcontext(_:_:))*