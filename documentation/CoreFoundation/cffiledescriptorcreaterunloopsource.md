# CFFileDescriptorCreateRunLoopSource(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Creates a new runloop source for a given CFFileDescriptor.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func CFFileDescriptorCreateRunLoopSource(_ allocator: CFAllocator!, _ f: CFFileDescriptor!, _ order: CFIndex) -> CFRunLoopSource!
```

#### Return Value

A new runloop source for `f`, or `NULL` if there was a problem creating the object. Ownership follows the [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

#### Discussion

The context for the new runloop (see [`CFRunLoopSourceCreate(_:_:_:)`](cfrunloopsourcecreate(_:_:_:).md)) is the same as the context passed in when the CFFileDescriptor was created (see [`CFFileDescriptorCreate(_:_:_:_:_:)`](cffiledescriptorcreate(_:_:_:_:_:).md)).

## Parameters

- `allocator`: The allocator to use to allocate memory for the new bag and its storage for values. Pass   or kCFAllocatorDefault to use the current default allocator.
- `f`: A CFFileDescriptor.
- `order`: The order for the new run loop (see  ).


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cffiledescriptorcreaterunloopsource(_:_:_:))*