# CFFileDescriptorDisableCallBacks(_:_:)

**Framework**: Core Foundation  
**Kind**: func

Disables callbacks for a given CFFileDescriptor.

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
func CFFileDescriptorDisableCallBacks(_ f: CFFileDescriptor!, _ callBackTypes: CFOptionFlags)
```

## Parameters

- `f`: A CFFileDescriptor.
- `callBackTypes`: A bitmask that specifies which callbacks to disable (see   for possible components).

## See Also

- [func CFFileDescriptorEnableCallBacks(CFFileDescriptor!, CFOptionFlags)](cffiledescriptorenablecallbacks(_:_:).md)
  Enables callbacks for a given CFFileDescriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cffiledescriptordisablecallbacks(_:_:))*