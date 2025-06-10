# port(withMachPort:options:)

**Framework**: Foundation  
**Kind**: method

Creates and returns a port object configured with the specified options and the given Mach port.

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
class func port(withMachPort machPort: UInt32, options f: NSMachPort.Options = []) -> Port
```

#### Return Value

An `NSMachPort` object that uses `machPort` to send or receive messages.

#### Discussion

Creates the port object if necessary. Depending on the access rights associated with `machPort`, the new port object may be usable only for sending messages.

## Parameters

- `machPort`: The Mach port for the new port. This parameter should originally be of type mach_port_t.
- `f`: Specifies options for what to do with the underlying port rights when the   object is invalidated or destroyed. For a list of constants, see  .

## See Also

- [class func port(withMachPort: UInt32) -> Port](nsmachport/port(withmachport:).md)
  Creates and returns a port object configured with the given Mach port.
- [init(machPort: UInt32)](nsmachport/init(machport:).md)
  Initializes a newly allocated `NSMachPort` object with a given Mach port.
- [init(machPort: UInt32, options: NSMachPort.Options)](nsmachport/init(machport:options:).md)
  Initializes a newly allocated `NSMachPort` object with a given Mach port and the specified options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmachport/port(withmachport:options:))*