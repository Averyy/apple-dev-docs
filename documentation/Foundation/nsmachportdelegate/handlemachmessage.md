# handleMachMessage(_:)

**Framework**: Foundation  
**Kind**: method

Process an incoming Mach message.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
optional func handleMachMessage(_ msg: UnsafeMutableRawPointer)
```

#### Discussion

The delegate should interpret this data as a pointer to a Mach message beginning with a msg_header_t structure and should handle the message appropriately.

The delegate should implement either `handleMachMessage:` or the [`PortDelegate`](portdelegate.md) protocol method handlePortMessage:.

## Parameters

- `msg`: A pointer to a Mach message, cast as a pointer to void.

## See Also

- [Distributed Objects Programming Topics](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DistrObjects/DistrObjects.html#//apple_ref/doc/uid/10000102i)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmachportdelegate/handlemachmessage(_:))*