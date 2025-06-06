# CFSocket

**Framework**: Core Foundation  
**Kind**: class

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
class CFSocket
```

#### Overview

A CFSocket is a communications channel implemented with a BSD socket.

For most uses of this API, you will need to include three headers:

```objc
#import <CoreFoundation/CoreFoundation.h> #include <sys/socket.h> #include <netinet/in.h>
```

CFSocket can be created from scratch with [`CFSocketCreate(_:_:_:_:_:_:_:)`](cfsocketcreate(_:_:_:_:_:_:_:).md) and [`CFSocketCreateWithSocketSignature(_:_:_:_:_:)`](cfsocketcreatewithsocketsignature(_:_:_:_:_:).md). CFSocket objects can also be created to wrap an existing BSD socket by calling [`CFSocketCreateWithNative(_:_:_:_:_:)`](cfsocketcreatewithnative(_:_:_:_:_:).md). Finally, you can create a CFSocket and connect simultaneously to a remote host by calling [`CFSocketCreateConnectedToSocketSignature(_:_:_:_:_:_:)`](cfsocketcreateconnectedtosocketsignature(_:_:_:_:_:_:).md).

To listen for messages, you need to create a run loop source with [`CFSocketCreateRunLoopSource(_:_:_:)`](cfsocketcreaterunloopsource(_:_:_:).md) and add it to a run loop with [`CFRunLoopAddSource(_:_:_:)`](cfrunloopaddsource(_:_:_:).md). You can select the types of socket activities, such as connection attempts or data arrivals, that cause the source to fire and invoke your CFSocket’s callback function. To send data, you store the data in a CFData and call [`CFSocketSendData(_:_:_:_:)`](cfsocketsenddata(_:_:_:_:).md).

Unlike Mach and message ports, sockets support communication over a network.

## Topics

### Creating Sockets
- [func CFSocketCreate(CFAllocator!, Int32, Int32, Int32, CFOptionFlags, CFSocketCallBack!, UnsafePointer<CFSocketContext>!) -> CFSocket!](cfsocketcreate(_:_:_:_:_:_:_:).md)
  Creates a CFSocket object of a specified protocol and type.
- [func CFSocketCreateConnectedToSocketSignature(CFAllocator!, UnsafePointer<CFSocketSignature>!, CFOptionFlags, CFSocketCallBack!, UnsafePointer<CFSocketContext>!, CFTimeInterval) -> CFSocket!](cfsocketcreateconnectedtosocketsignature(_:_:_:_:_:_:).md)
  Creates a CFSocket object and opens a connection to a remote socket.
- [func CFSocketCreateWithNative(CFAllocator!, CFSocketNativeHandle, CFOptionFlags, CFSocketCallBack!, UnsafePointer<CFSocketContext>!) -> CFSocket!](cfsocketcreatewithnative(_:_:_:_:_:).md)
  Creates a CFSocket object for a pre-existing native socket.
- [func CFSocketCreateWithSocketSignature(CFAllocator!, UnsafePointer<CFSocketSignature>!, CFOptionFlags, CFSocketCallBack!, UnsafePointer<CFSocketContext>!) -> CFSocket!](cfsocketcreatewithsocketsignature(_:_:_:_:_:).md)
  Creates a CFSocket object using information from a CFSocketSignature structure.
### Configuring Sockets
- [func CFSocketCopyAddress(CFSocket!) -> CFData!](cfsocketcopyaddress(_:).md)
  Returns the local address of a CFSocket object.
- [func CFSocketCopyPeerAddress(CFSocket!) -> CFData!](cfsocketcopypeeraddress(_:).md)
  Returns the remote address to which a CFSocket object is connected.
- [func CFSocketDisableCallBacks(CFSocket!, CFOptionFlags)](cfsocketdisablecallbacks(_:_:).md)
  Disables the callback function of a CFSocket object for certain types of socket activity.
- [func CFSocketEnableCallBacks(CFSocket!, CFOptionFlags)](cfsocketenablecallbacks(_:_:).md)
  Enables the callback function of a CFSocket object for certain types of socket activity.
- [func CFSocketGetContext(CFSocket!, UnsafeMutablePointer<CFSocketContext>!)](cfsocketgetcontext(_:_:).md)
  Returns the context information for a CFSocket object.
- [func CFSocketGetNative(CFSocket!) -> CFSocketNativeHandle](cfsocketgetnative(_:).md)
  Returns the native socket associated with a CFSocket object.
- [func CFSocketGetSocketFlags(CFSocket!) -> CFOptionFlags](cfsocketgetsocketflags(_:).md)
  Returns flags that control certain behaviors of a CFSocket object.
- [func CFSocketSetAddress(CFSocket!, CFData!) -> CFSocketError](cfsocketsetaddress(_:_:).md)
  Binds a local address to a CFSocket object and configures it for listening.
- [func CFSocketSetSocketFlags(CFSocket!, CFOptionFlags)](cfsocketsetsocketflags(_:_:).md)
  Sets flags that control certain behaviors of a CFSocket object.
### Using Sockets
- [func CFSocketConnectToAddress(CFSocket!, CFData!, CFTimeInterval) -> CFSocketError](cfsocketconnecttoaddress(_:_:_:).md)
  Opens a connection to a remote socket.
- [func CFSocketCreateRunLoopSource(CFAllocator!, CFSocket!, CFIndex) -> CFRunLoopSource!](cfsocketcreaterunloopsource(_:_:_:).md)
  Creates a CFRunLoopSource object for a CFSocket object.
- [func CFSocketGetTypeID() -> CFTypeID](cfsocketgettypeid().md)
  Returns the type identifier for the CFSocket opaque type.
- [func CFSocketInvalidate(CFSocket!)](cfsocketinvalidate(_:).md)
  Invalidates a CFSocket object, stopping it from sending or receiving any more messages.
- [func CFSocketIsValid(CFSocket!) -> Bool](cfsocketisvalid(_:).md)
  Returns a Boolean value that indicates whether a CFSocket object is valid and able to send or receive messages.
- [func CFSocketSendData(CFSocket!, CFData!, CFData!, CFTimeInterval) -> CFSocketError](cfsocketsenddata(_:_:_:_:).md)
  Sends data over a CFSocket object.
### Callbacks
- [typealias CFSocketCallBack](cfsocketcallback.md)
  Callback invoked when certain types of activity takes place on a CFSocket object.
### Data Types
- [struct CFSocketContext](cfsocketcontext.md)
  A structure that contains program-defined data and callbacks with which you can configure a CFSocket object’s behavior.
- [typealias CFSocketNativeHandle](cfsocketnativehandle.md)
  Type for the platform-specific native socket handle.
- [struct CFSocketSignature](cfsocketsignature.md)
  A structure that fully specifies the communication protocol and connection address of a CFSocket object.
### Constants
- [struct CFSocketCallBackType](cfsocketcallbacktype.md)
  Types of socket activity that can cause the callback function of a CFSocket object to be called.
- [CFSocket Flags](1560944-cfsocket-flags.md)
  Flags that can be set on a CFSocket object to control its behavior.
- [enum CFSocketError](cfsocketerror.md)
  Error codes for many CFSocket functions.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [Threading Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Multithreading/Introduction/Introduction.html#//apple_ref/doc/uid/10000057i)
- [CFNetwork Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Networking/Conceptual/CFNetwork/Introduction/Introduction.html#//apple_ref/doc/uid/TP30001132)
- [class CFAllocator](cfallocator.md)
- [class CFArray](cfarray.md)
- [class CFAttributedString](cfattributedstring.md)
- [class CFBag](cfbag.md)
- [class CFBinaryHeap](cfbinaryheap.md)
- [class CFBitVector](cfbitvector.md)
- [class CFBoolean](cfboolean.md)
- [class CFBundle](cfbundle.md)
- [class CFCalendar](cfcalendar.md)
- [class CFCharacterSet](cfcharacterset.md)
- [class CFData](cfdata.md)
- [class CFDate](cfdate.md)
- [class CFDateFormatter](cfdateformatter.md)
- [class CFDictionary](cfdictionary.md)
- [class CFError](cferror.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfsocket)*