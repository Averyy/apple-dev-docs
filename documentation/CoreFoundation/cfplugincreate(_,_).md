# CFPlugInCreate(_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Creates a CFPlugIn given its URL.

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
func CFPlugInCreate(_ allocator: CFAllocator!, _ plugInURL: CFURL!) -> CFPlugIn!
```

```c
extern CFPlugInRefCFPlugInCreate(CFAllocatorRef allocator, CFURLRef plugInURL);
```

## Return Value

A new plug-in. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Parameters

- `allocator`: The allocator to use to allocate memory for the new plug-in. Pass `NULL` or kCFAllocatorDefault to use the default allocator.
- `plugInURL`: The location of the plug-in.

## See Also

### Creating Plug-ins
- [func CFPlugInInstanceCreate(CFAllocator!, CFUUID!, CFUUID!) -> UnsafeMutableRawPointer!](./cfplugininstancecreate%28_,_,_%29.md)
  Creates a `CFPlugIn` instance of a given type using a given factory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfplugincreate(_:_:))*