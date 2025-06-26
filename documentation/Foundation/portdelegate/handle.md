# handle(_:)

**Framework**: Foundation  
**Kind**: method

Processes a given incoming message on the port.

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
optional func handle(_ message: PortMessage)
```

#### Discussion

See [`Port`](port.md) for more information.

The delegate should implement either [`handle(_:)`](portdelegate/handle(_:).md) or the [`NSMachPortDelegate`](nsmachportdelegate.md) protocol method [`handleMachMessage(_:)`](nsmachportdelegate/handlemachmessage(_:).md). You must not implement both delegate methods.

## Parameters

- `message`: An incoming port message.

## See Also

- [Distributed Objects Programming Topics](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DistrObjects/DistrObjects.html#//apple_ref/doc/uid/10000102i)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/portdelegate/handle(_:))*