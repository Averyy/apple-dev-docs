# Mach.Port

**Framework**: System  
**Kind**: struct

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- macOS 14.4+
- tvOS 17.4+
- visionOS 1.0+
- watchOS 10.4+

## Declaration

```swift
struct Port<RightType> where RightType : MachPortRight
```

## Topics

### Initializers
- [init()](mach/port/init.md)
  Allocate a new Mach port with a receive right, creating a Mach.Port<Mach.ReceiveRight> to manage it.
- [init(name: mach_port_name_t)](mach/port/init(name:).md)
  Transfer ownership of an existing unmanaged Mach port right into a `Mach.Port` by name.
- [init(name: mach_port_name_t, context: mach_port_context_t)](mach/port/init(name:context:)-14mp9.md)
  Transfer ownership of an existing, unmanaged, but already guarded, Mach port right into a Mach.Port by name.
- [init(name: mach_port_name_t, context: mach_port_context_t)](mach/port/init(name:context:)-oyjl.md)
  Transfer ownership of an existing, unmanaged, but already guarded, Mach port right into a Mach.Port by name.
### Instance Properties
- [var makeSendCount: mach_port_mscount_t](mach/port/makesendcount.md)
  Access the make-send count.
### Instance Methods
- [func copySendRight() throws -> Mach.Port<Mach.SendRight>](mach/port/copysendright.md)
  Create another send right from a given send right.
- [func makeSendOnceRight() -> Mach.Port<Mach.SendOnceRight>](mach/port/makesendonceright.md)
  Create a send-once right for a given receive right.
- [func makeSendRight() -> Mach.Port<Mach.SendRight>](mach/port/makesendright.md)
  Create a send right for a given receive right.
- [func relinquish() -> mach_port_name_t](mach/port/relinquish-241tg.md)
  Transfer ownership of the underlying port right to the caller.
- [func relinquish() -> (name: mach_port_name_t, context: mach_port_context_t)](mach/port/relinquish-70vbe.md)
  Transfer ownership of the underlying port right to the caller.
- [func relinquish() -> mach_port_name_t](mach/port/relinquish-74amu.md)
  Transfer ownership of the underlying port right to the caller.
- [func relinquish() -> (name: mach_port_name_t, context: mach_port_context_t)](mach/port/relinquish-9lm56.md)
  Transfer ownership of the underlying port right to the caller.
- [func unguardAndRelinquish() -> mach_port_name_t](mach/port/unguardandrelinquish.md)
  Remove guard and transfer ownership of the underlying port right to the caller.
- [func withBorrowedName<ReturnType>(body: (mach_port_name_t, mach_port_context_t) -> ReturnType) -> ReturnType](mach/port/withborrowedname(body:)-4d4iq.md)
  Borrow access to the port name in a block that can perform non-consuming operations.
- [func withBorrowedName<ReturnType>(body: (mach_port_name_t, mach_port_context_t) -> ReturnType) -> ReturnType](mach/port/withborrowedname(body:)-8402i.md)
  Borrow access to the port name in a block that can perform non-consuming operations.
- [func withBorrowedName<ReturnType>(body: (mach_port_name_t) -> ReturnType) -> ReturnType](mach/port/withborrowedname(body:)-9v68k.md)
  Borrow access to the port name in a block that can perform non-consuming operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/mach/port)*