# port(withMachPort:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Creates and returns a port object configured with the given Mach port.

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
class func port(withMachPort machPort: UInt32) -> Port
```

```objc
+ (NSPort *) portWithMachPort:(uint32_t) machPort;
```

## Return Value

An `NSMachPort` object that uses `machPort` to send or receive messages.

## Discussion

Creates the port object if necessary. Depending on the access rights associated with `machPort`, the new port object may be usable only for sending messages.

## Parameters

- `machPort`: The Mach port for the new port. This parameter should originally be of type mach_port_t.

## See Also

### Related Documentation
- [Distributed Objects Programming Topics](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DistrObjects/DistrObjects.html#//apple_ref/doc/uid/10000102i)
### Creating and Initializing
- [class func port(withMachPort: UInt32, options: NSMachPort.Options) -> Port](./port%28withmachport,options%29.md)
  Creates and returns a port object configured with the specified options and the given Mach port.
- [init(machPort: UInt32)](./init%28machport%29.md)
  Initializes a newly allocated `NSMachPort` object with a given Mach port.
- [init(machPort: UInt32, options: NSMachPort.Options)](./init%28machport,options%29.md)
  Initializes a newly allocated `NSMachPort` object with a given Mach port and the specified options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmachport/port(withmachport:))*