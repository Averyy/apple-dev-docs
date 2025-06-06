# CFFileDescriptorEnableCallBacks(_:_:)

**Framework**: Core Foundation  
**Kind**: func

Enables callbacks for a given CFFileDescriptor.

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
func CFFileDescriptorEnableCallBacks(_ f: CFFileDescriptor!, _ callBackTypes: CFOptionFlags)
```

## Parameters

- `f`: A CFFileDescriptor.
- `callBackTypes`: A bitmask that specifies which callbacks to enable (see   for possible components).

## See Also

- [func CFFileDescriptorDisableCallBacks(CFFileDescriptor!, CFOptionFlags)](cffiledescriptordisablecallbacks(_:_:).md)
  Disables callbacks for a given CFFileDescriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cffiledescriptorenablecallbacks(_:_:))*