# Mach.Port

**Framework**: System  
**Kind**: struct  
**Role**: Structure

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
- [init()](./port/init%28%29.md)
  Allocate a new Mach port with a receive right, creating a Mach.Port<Mach.ReceiveRight> to manage it.
- [init(name: mach_port_name_t)](./port/init%28name%29.md)
  Transfer ownership of an existing unmanaged Mach port right into a `Mach.Port` by name.
- [init(name: mach_port_name_t, context: mach_port_context_t)](./port/init%28name,context%29-14mp9.md)
  Transfer ownership of an existing, unmanaged, but already guarded, Mach port right into a Mach.Port by name.
- [init(name: mach_port_name_t, context: mach_port_context_t)](./port/init%28name,context%29-oyjl.md)
  Transfer ownership of an existing, unmanaged, but already guarded, Mach port right into a Mach.Port by name.
### Instance Properties
- [var makeSendCount: mach_port_mscount_t](./port/makesendcount.md)
  Access the make-send count.
### Instance Methods
- [func copySendRight() throws -> Mach.Port<Mach.SendRight>](./port/copysendright%28%29.md)
  Create another send right from a given send right.
- [func makeSendOnceRight() -> Mach.Port<Mach.SendOnceRight>](./port/makesendonceright%28%29.md)
  Create a send-once right for a given receive right.
- [func makeSendRight() -> Mach.Port<Mach.SendRight>](./port/makesendright%28%29.md)
  Create a send right for a given receive right.
- [func relinquish() -> mach_port_name_t](./port/relinquish%28%29-241tg.md)
  Transfer ownership of the underlying port right to the caller.
- [func relinquish() -> (name: mach_port_name_t, context: mach_port_context_t)](./port/relinquish%28%29-70vbe.md)
  Transfer ownership of the underlying port right to the caller.
- [func relinquish() -> mach_port_name_t](./port/relinquish%28%29-74amu.md)
  Transfer ownership of the underlying port right to the caller.
- [func relinquish() -> (name: mach_port_name_t, context: mach_port_context_t)](./port/relinquish%28%29-9lm56.md)
  Transfer ownership of the underlying port right to the caller.
- [func unguardAndRelinquish() -> mach_port_name_t](./port/unguardandrelinquish%28%29.md)
  Remove guard and transfer ownership of the underlying port right to the caller.
- [func withBorrowedName<ReturnType>(body: (mach_port_name_t, mach_port_context_t) -> ReturnType) -> ReturnType](./port/withborrowedname%28body%29-4d4iq.md)
  Borrow access to the port name in a block that can perform non-consuming operations.
- [func withBorrowedName<ReturnType>(body: (mach_port_name_t, mach_port_context_t) -> ReturnType) -> ReturnType](./port/withborrowedname%28body%29-8402i.md)
  Borrow access to the port name in a block that can perform non-consuming operations.
- [func withBorrowedName<ReturnType>(body: (mach_port_name_t) -> ReturnType) -> ReturnType](./port/withborrowedname%28body%29-9v68k.md)
  Borrow access to the port name in a block that can perform non-consuming operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/mach/port)*