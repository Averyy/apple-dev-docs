# CFMachPort

**Framework**: Core Foundation  
**Kind**: class  
**Role**: Class

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
class CFMachPort
```

```c
typedef struct __CFMachPort * CFMachPortRef;
```

## Overview

A CFMachPort object is a wrapper for a native Mach port (`mach_port_t`). Mach ports are the native communication channel for the macOS kernel.

CFMachPort does not provide a function to send messages, so you primarily use a CFMachPort object if you need to listen to a Mach port that you obtained by other means. You can get a callback when a message arrives on the port or when the port becomes invalid, such as when the native port dies.

To listen for messages you need to create a run loop source with [`CFMachPortCreateRunLoopSource(_:_:_:)`](./cfmachportcreaterunloopsource%28_,_,_%29.md) and add it to a run loop with [`CFRunLoopAddSource(_:_:_:)`](./cfrunloopaddsource%28_,_,_%29.md).

> ❗ **Important**:  If you want to tear down the connection, you must invalidate the port (using [`CFMachPortInvalidate(_:)`](./cfmachportinvalidate%28_%29.md)) before releasing the runloop source and the Mach port object.

To send data, you must use the Mach APIs with the native Mach port, which is not described here. Alternatively, you can use a [`CFMessagePort`](./cfmessageport.md) object, which can send arbitrary data.

Mach ports only support communication on the local machine. For network communication, you have to use a [`CFSocket`](./cfsocket.md) object.

## Topics

### Creating a CFMachPort Object
- [func CFMachPortCreate(CFAllocator!, CFMachPortCallBack!, UnsafeMutablePointer<CFMachPortContext>!, UnsafeMutablePointer<DarwinBoolean>!) -> CFMachPort!](./cfmachportcreate%28_,_,_,_%29.md)
  Creates a CFMachPort object with a new Mach port.
- [func CFMachPortCreateWithPort(CFAllocator!, mach_port_t, CFMachPortCallBack!, UnsafeMutablePointer<CFMachPortContext>!, UnsafeMutablePointer<DarwinBoolean>!) -> CFMachPort!](./cfmachportcreatewithport%28_,_,_,_,_%29.md)
  Creates a CFMachPort object for a pre-existing native Mach port.
### Configuring a CFMachPort Object
- [func CFMachPortInvalidate(CFMachPort!)](./cfmachportinvalidate%28_%29.md)
  Invalidates a CFMachPort object, stopping it from receiving any more messages.
- [func CFMachPortCreateRunLoopSource(CFAllocator!, CFMachPort!, CFIndex) -> CFRunLoopSource!](./cfmachportcreaterunloopsource%28_,_,_%29.md)
  Creates a CFRunLoopSource object for a CFMachPort object.
- [func CFMachPortSetInvalidationCallBack(CFMachPort!, CFMachPortInvalidationCallBack!)](./cfmachportsetinvalidationcallback%28_,_%29.md)
  Sets the callback function invoked when a CFMachPort object is invalidated.
### Examining a CFMachPort Object
- [func CFMachPortGetContext(CFMachPort!, UnsafeMutablePointer<CFMachPortContext>!)](./cfmachportgetcontext%28_,_%29.md)
  Returns the context information for a CFMachPort object.
- [func CFMachPortGetInvalidationCallBack(CFMachPort!) -> CFMachPortInvalidationCallBack!](./cfmachportgetinvalidationcallback%28_%29.md)
  Returns the invalidation callback function for a CFMachPort object.
- [func CFMachPortGetPort(CFMachPort!) -> mach_port_t](./cfmachportgetport%28_%29.md)
  Returns the native Mach port represented by a CFMachPort object.
- [func CFMachPortIsValid(CFMachPort!) -> Bool](./cfmachportisvalid%28_%29.md)
  Returns a Boolean value that indicates whether a CFMachPort object is valid and able to receive messages.
### Getting the CFMachPort Type ID
- [func CFMachPortGetTypeID() -> CFTypeID](./cfmachportgettypeid%28%29.md)
  Returns the type identifier for the CFMachPort opaque type.
### Callbacks
- [typealias CFMachPortCallBack](./cfmachportcallback.md)
  Callback invoked to process a message received on a CFMachPort object.
- [typealias CFMachPortInvalidationCallBack](./cfmachportinvalidationcallback.md)
  Callback invoked when a CFMachPort object is invalidated.
### Data Types
- [struct CFMachPortContext](./cfmachportcontext.md)
  A structure that contains program-defined data and callbacks with which you can configure a CFMachPort object’s behavior.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)

## See Also

### Opaque Types
- [class CFAllocator](./cfallocator.md)
- [class CFArray](./cfarray.md)
- [class CFAttributedString](./cfattributedstring.md)
- [class CFBag](./cfbag.md)
- [class CFBinaryHeap](./cfbinaryheap.md)
- [class CFBitVector](./cfbitvector.md)
- [class CFBoolean](./cfboolean.md)
- [class CFBundle](./cfbundle.md)
- [class CFCalendar](./cfcalendar.md)
- [class CFCharacterSet](./cfcharacterset.md)
- [class CFData](./cfdata.md)
- [class CFDate](./cfdate.md)
- [class CFDateFormatter](./cfdateformatter.md)
- [class CFDictionary](./cfdictionary.md)
- [class CFError](./cferror.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfmachport)*