# CFFileDescriptorInvalidate(_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Invalidates a CFFileDescriptor object.

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
func CFFileDescriptorInvalidate(_ f: CFFileDescriptor!)
```

```c
extern void CFFileDescriptorInvalidate(CFFileDescriptorRef f);
```

#### Discussion

Once invalidated, the CFFileDescriptor object will no longer be read from or written to at the Core Fundation level.

If you passed `true` for the `closeOnInvalidate` parameter when you called [`CFFileDescriptorCreate(_:_:_:_:_:)`](./cffiledescriptorcreate%28_,_,_,_,_%29.md), this function also closes the underlying file descriptor. If you passed `false`, you must close the descriptor yourself *after* invalidating the CFFileDescriptor object.

> ❗ **Important**:  You must invalidate the CFFileDescriptor before closing the underlying file descriptor.

## Parameters

- `f`: A CFFileDescriptor.

## See Also

### Related Documentation
- [func CFFileDescriptorGetNativeDescriptor(CFFileDescriptor!) -> CFFileDescriptorNativeDescriptor](./cffiledescriptorgetnativedescriptor%28_%29.md)
  Returns the native file descriptor for a given CFFileDescriptor.
- [func CFFileDescriptorIsValid(CFFileDescriptor!) -> Bool](./cffiledescriptorisvalid%28_%29.md)
  Returns a Boolean value that indicates whether the native file descriptor for a given CFFileDescriptor is valid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cffiledescriptorinvalidate(_:))*