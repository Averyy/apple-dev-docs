# init(machPort:options:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

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

```objc
- (instancetype) initWithMachPort:(uint32_t) machPort options:(NSMachPortOptions) f;
```

#### Return Value

Returns an initialized `NSMachPort` object that uses `machPort` to send or receive messages. The returned object might be different than the original receiver

#### Discussion

Depending on the access rights for `machPort`, the new port may be able to only send messages. If a port with `machPort` already exists, this method deallocates the receiver, then retains and returns the existing port.

## Parameters

- `machPort`: The Mach port for the new port. This parameter should originally be of type mach_port_t.
- `f`: Specifies options for what to do with the underlying port rights when the `NSMachPort` object is invalidated or destroyed. For a list of constants, see `Mach Port Rights`.

## See Also

### Creating and Initializing
- [class func port(withMachPort: UInt32) -> Port](./port%28withmachport%29.md)
  Creates and returns a port object configured with the given Mach port.
- [class func port(withMachPort: UInt32, options: NSMachPort.Options) -> Port](./port%28withmachport,options%29.md)
  Creates and returns a port object configured with the specified options and the given Mach port.
- [init(machPort: UInt32)](./init%28machport%29.md)
  Initializes a newly allocated `NSMachPort` object with a given Mach port.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmachport/init(machport:options:))*