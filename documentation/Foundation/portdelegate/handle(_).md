# handle(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

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

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```swift
optional func handle(_ message: NSPortMessage)
```

*Mac Catalyst, macOS*

```swift
optional func handle(_ message: PortMessage)
```

```objc
- (void) handlePortMessage:(NSPortMessage *) message;
```

## Discussion

See [`Port`](../port.md) for more information.

The delegate should implement either [`handle(_:)`](./handle%28_%29.md) or the [`NSMachPortDelegate`](../nsmachportdelegate.md) protocol method [`handleMachMessage(_:)`](../nsmachportdelegate/handlemachmessage%28_%29.md). You must not implement both delegate methods.

## Parameters

- `message`: An incoming port message.

## See Also

### Related Documentation
- [Distributed Objects Programming Topics](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DistrObjects/DistrObjects.html#//apple_ref/doc/uid/10000102i)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/portdelegate/handle(_:))*