# init(machPort:options:)

**Framework**: Foundation  
**Kind**: init

Initializes a newly allocated `NSMachPort` object with a given Mach port and the specified options.

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
init(machPort: UInt32, options f: NSMachPort.Options = [])
```

#### Return Value

Returns an initialized `NSMachPort` object that uses `machPort` to send or receive messages. The returned object might be different than the original receiver

#### Discussion

Depending on the access rights for `machPort`, the new port may be able to only send messages. If a port with `machPort` already exists, this method deallocates the receiver, then retains and returns the existing port.

## Parameters

- `machPort`: The Mach port for the new port. This parameter should originally be of type mach_port_t.
- `f`: Specifies options for what to do with the underlying port rights when the   object is invalidated or destroyed. For a list of constants, see  .

## See Also

- [class func port(withMachPort: UInt32) -> Port](nsmachport/port(withmachport:).md)
  Creates and returns a port object configured with the given Mach port.
- [class func port(withMachPort: UInt32, options: NSMachPort.Options) -> Port](nsmachport/port(withmachport:options:).md)
  Creates and returns a port object configured with the specified options and the given Mach port.
- [init(machPort: UInt32)](nsmachport/init(machport:).md)
  Initializes a newly allocated `NSMachPort` object with a given Mach port.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmachport/init(machport:options:))*