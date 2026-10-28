# CFMessagePort

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
class CFMessagePort
```

```c
typedef struct __CFMessagePort * CFMessagePortRef;
```

## Overview

CFMessagePort objects provide a communications channel that can transmit arbitrary data between multiple threads or processes on the local machine.

You create a local message port with [`CFMessagePortCreateLocal(_:_:_:_:_:)`](./cfmessageportcreatelocal%28_,_,_,_,_%29.md) and make it available to other processes by giving it a name, either when you create it or later with [`CFMessagePortSetName(_:_:)`](./cfmessageportsetname%28_,_%29.md). Other processes then connect to it using [`CFMessagePortCreateRemote(_:_:)`](./cfmessageportcreateremote%28_,_%29.md), specifying the name of the port.

To listen for messages, you need to create a run loop source with [`CFMessagePortCreateRunLoopSource(_:_:_:)`](./cfmessageportcreaterunloopsource%28_,_,_%29.md) and add it to a run loop with [`CFRunLoopAddSource(_:_:_:)`](./cfrunloopaddsource%28_,_,_%29.md).

> ❗ **Important**:  If you want to tear down the connection, you must invalidate the port (using [`CFMessagePortInvalidate(_:)`](./cfmessageportinvalidate%28_%29.md)) before releasing the runloop source and the message port object.

Your message port’s callback function will be called when a message arrives. To send data, you store the data in a CFData object and call [`CFMessagePortSendRequest(_:_:_:_:_:_:_:)`](./cfmessageportsendrequest%28_,_,_,_,_,_,_%29.md). You can optionally have the function wait for a reply and return the reply in another CFData object.

Message ports only support communication on the local machine. For network communication, you have to use a [`CFSocket`](./cfsocket.md) object.

## Topics

### Creating a CFMessagePort Object
- [func CFMessagePortCreateLocal(CFAllocator!, CFString!, CFMessagePortCallBack!, UnsafeMutablePointer<CFMessagePortContext>!, UnsafeMutablePointer<DarwinBoolean>!) -> CFMessagePort!](./cfmessageportcreatelocal%28_,_,_,_,_%29.md)
  Returns a local CFMessagePort object.
- [func CFMessagePortCreateRemote(CFAllocator!, CFString!) -> CFMessagePort!](./cfmessageportcreateremote%28_,_%29.md)
  Returns a CFMessagePort object connected to a remote port.
### Configuring a CFMessagePort Object
- [func CFMessagePortCreateRunLoopSource(CFAllocator!, CFMessagePort!, CFIndex) -> CFRunLoopSource!](./cfmessageportcreaterunloopsource%28_,_,_%29.md)
  Creates a CFRunLoopSource object for a CFMessagePort object.
- [func CFMessagePortSetInvalidationCallBack(CFMessagePort!, CFMessagePortInvalidationCallBack!)](./cfmessageportsetinvalidationcallback%28_,_%29.md)
  Sets the callback function invoked when a CFMessagePort object is invalidated.
- [func CFMessagePortSetName(CFMessagePort!, CFString!) -> Bool](./cfmessageportsetname%28_,_%29.md)
  Sets the name of a local CFMessagePort object.
### Using a Message Port
- [func CFMessagePortInvalidate(CFMessagePort!)](./cfmessageportinvalidate%28_%29.md)
  Invalidates a CFMessagePort object, stopping it from receiving or sending any more messages.
- [func CFMessagePortSendRequest(CFMessagePort!, Int32, CFData!, CFTimeInterval, CFTimeInterval, CFString!, UnsafeMutablePointer<Unmanaged<CFData>?>!) -> Int32](./cfmessageportsendrequest%28_,_,_,_,_,_,_%29.md)
  Sends a message to a remote CFMessagePort object.
- [func CFMessagePortSetDispatchQueue(CFMessagePort!, dispatch_queue_t!)](./cfmessageportsetdispatchqueue%28_,_%29.md)
  Schedules callbacks for the specified message port on the specified dispatch queue.
### Examining a Message Port
- [func CFMessagePortGetContext(CFMessagePort!, UnsafeMutablePointer<CFMessagePortContext>!)](./cfmessageportgetcontext%28_,_%29.md)
  Returns the context information for a CFMessagePort object.
- [func CFMessagePortGetInvalidationCallBack(CFMessagePort!) -> CFMessagePortInvalidationCallBack!](./cfmessageportgetinvalidationcallback%28_%29.md)
  Returns the invalidation callback function for a CFMessagePort object.
- [func CFMessagePortGetName(CFMessagePort!) -> CFString!](./cfmessageportgetname%28_%29.md)
  Returns the name with which a CFMessagePort object is registered.
- [func CFMessagePortIsRemote(CFMessagePort!) -> Bool](./cfmessageportisremote%28_%29.md)
  Returns a Boolean value that indicates whether a CFMessagePort object represents a remote port.
- [func CFMessagePortIsValid(CFMessagePort!) -> Bool](./cfmessageportisvalid%28_%29.md)
  Returns a Boolean value that indicates whether a CFMessagePort object is valid and able to send or receive messages.
### Getting the CFMessagePort Type ID
- [func CFMessagePortGetTypeID() -> CFTypeID](./cfmessageportgettypeid%28%29.md)
  Returns the type identifier for the CFMessagePort opaque type.
### Callbacks
- [typealias CFMessagePortCallBack](./cfmessageportcallback.md)
  Callback invoked to process a message received on a CFMessagePort object.
- [typealias CFMessagePortInvalidationCallBack](./cfmessageportinvalidationcallback.md)
  Callback invoked when a CFMessagePort object is invalidated.
### Data Types
- [struct CFMessagePortContext](./cfmessageportcontext.md)
  A structure that contains program-defined data and callbacks with which you can configure a CFMessagePort object’s behavior.
### Constants
- [CFMessagePortSendRequest Error Codes](./api-1561514-cfmessageportsendrequest-error-c.md)
  Error codes for `CFMessagePortSendRequest`.

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

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfmessageport)*