# CFNumberCreate(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Creates a CFNumber object using a specified value.

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
func CFNumberCreate(_ allocator: CFAllocator!, _ theType: CFNumberType, _ valuePtr: UnsafeRawPointer!) -> CFNumber!
```

```c
extern CFNumberRefCFNumberCreate(CFAllocatorRef allocator, CFNumberType theType, const void *valuePtr);
```

#### Return Value

A new number with the value specified by `valuePtr`. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

#### Discussion

The `theType` parameter is not necessarily preserved when creating a new CFNumber object. The CFNumber object will be created using whatever internal storage type the creation function deems appropriate. Use the function [`CFNumberGetType(_:)`](./cfnumbergettype%28_%29.md) to find out what type the CFNumber object used to store your value.

## Parameters

- `allocator`: The allocator to use to allocate memory for the new object. Pass `NULL` or kCFAllocatorDefault to use the default allocator.
- `theType`: A constant that specifies the data type of the value to convert. See [`CFNumberType`](./cfnumbertype.md) for a list of possible values.
- `valuePtr`: A pointer to the value for the returned number object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfnumbercreate(_:_:_:))*