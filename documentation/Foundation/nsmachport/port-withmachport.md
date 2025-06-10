# port(withMachPort:)

**Framework**: Foundation  
**Kind**: method

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

#### Return Value

An `NSMachPort` object that uses `machPort` to send or receive messages.

#### Discussion

Creates the port object if necessary. Depending on the access rights associated with `machPort`, the new port object may be usable only for sending messages.

## Parameters

- `machPort`: The Mach port for the new port. This parameter should originally be of type mach_port_t.

## See Also

- [Distributed Objects Programming Topics](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DistrObjects/DistrObjects.html#//apple_ref/doc/uid/10000102i)
- [class func port(withMachPort: UInt32, options: NSMachPort.Options) -> Port](nsmachport/port(withmachport:options:).md)
  Creates and returns a port object configured with the specified options and the given Mach port.
- [init(machPort: UInt32)](nsmachport/init(machport:).md)
  Initializes a newly allocated `NSMachPort` object with a given Mach port.
- [init(machPort: UInt32, options: NSMachPort.Options)](nsmachport/init(machport:options:).md)
  Initializes a newly allocated `NSMachPort` object with a given Mach port and the specified options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmachport/port(withmachport:))*