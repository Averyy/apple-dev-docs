# CFReadStream

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
class CFReadStream
```

```c
typedef struct __CFReadStream * CFReadStreamRef;
```

## Overview

`CFReadStream` provides an interface for reading a byte stream either synchronously or asynchronously. You can create streams that read bytes from a block of memory, a file, or a generic socket. All streams need to be opened, using [`CFReadStreamOpen(_:)`](./cfreadstreamopen%28_%29.md), before reading.

Use [`CFWriteStream`](./cfwritestream.md) for writing byte streams. The CFNetwork framework defines an additional type of stream for reading responses to HTTP requests.

CFReadStream is “toll-free bridged” with its Cocoa Foundation counterpart, [`InputStream`](../Foundation/inputstream.md). This means that the Core Foundation type is interchangeable in function or method calls with the bridged Foundation object. Therefore, in a method where you see an `NSInputStream *` parameter, you can pass in a CFReadStreamRef, and in a function where you see a CFReadStreamRef parameter, you can pass in an `NSInputStream` instance. Note, however, that you may have either a delegate or callbacks but not both. See [Toll-Free Bridged Types](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFDesignConcepts/Articles/tollFreeBridgedTypes.html#//apple_ref/doc/uid/TP40010677) for more information on toll-free bridging.

## Topics

### Creating a Read Stream
- [func CFReadStreamCreateWithBytesNoCopy(CFAllocator!, UnsafePointer<UInt8>!, CFIndex, CFAllocator!) -> CFReadStream!](./cfreadstreamcreatewithbytesnocopy%28_,_,_,_%29.md)
  Creates a readable stream for a block of memory.
- [func CFReadStreamCreateWithFile(CFAllocator!, CFURL!) -> CFReadStream!](./cfreadstreamcreatewithfile%28_,_%29.md)
  Creates a readable stream for a file.
### Opening and Closing a Read Stream
- [func CFReadStreamClose(CFReadStream!)](./cfreadstreamclose%28_%29.md)
  Closes a readable stream.
- [func CFReadStreamOpen(CFReadStream!) -> Bool](./cfreadstreamopen%28_%29.md)
  Opens a stream for reading.
### Reading from a Stream
- [func CFReadStreamRead(CFReadStream!, UnsafeMutablePointer<UInt8>!, CFIndex) -> CFIndex](./cfreadstreamread%28_,_,_%29.md)
  Reads data from a readable stream.
### Scheduling a Read Stream
- [func CFReadStreamScheduleWithRunLoop(CFReadStream!, CFRunLoop!, CFRunLoopMode!)](./cfreadstreamschedulewithrunloop%28_,_,_%29.md)
  Schedules a stream into a run loop.
- [func CFReadStreamUnscheduleFromRunLoop(CFReadStream!, CFRunLoop!, CFRunLoopMode!)](./cfreadstreamunschedulefromrunloop%28_,_,_%29.md)
  Removes a read stream from a given run loop.
### Examining Stream Properties
- [func CFReadStreamCopyProperty(CFReadStream!, CFStreamPropertyKey!) -> CFTypeRef!](./cfreadstreamcopyproperty%28_,_%29.md)
  Returns the value of a property for a stream.
- [func CFReadStreamGetBuffer(CFReadStream!, CFIndex, UnsafeMutablePointer<CFIndex>!) -> UnsafePointer<UInt8>!](./cfreadstreamgetbuffer%28_,_,_%29.md)
  Returns a pointer to a stream’s internal buffer of unread data, if possible.
- [func CFReadStreamCopyError(CFReadStream!) -> CFError!](./cfreadstreamcopyerror%28_%29.md)
  Returns the error associated with a stream.
- [func CFReadStreamGetError(CFReadStream!) -> CFStreamError](./cfreadstreamgeterror%28_%29.md)
  Returns the error status of a stream.
- [func CFReadStreamGetStatus(CFReadStream!) -> CFStreamStatus](./cfreadstreamgetstatus%28_%29.md)
  Returns the current state of a stream.
- [func CFReadStreamHasBytesAvailable(CFReadStream!) -> Bool](./cfreadstreamhasbytesavailable%28_%29.md)
  Returns a Boolean value that indicates whether a readable stream has data that can be read without blocking.
### Setting Stream Properties
- [func CFReadStreamSetClient(CFReadStream!, CFOptionFlags, CFReadStreamClientCallBack!, UnsafeMutablePointer<CFStreamClientContext>!) -> Bool](./cfreadstreamsetclient%28_,_,_,_%29.md)
  Assigns a client to a stream, which receives callbacks when certain events occur.
- [func CFReadStreamSetProperty(CFReadStream!, CFStreamPropertyKey!, CFTypeRef!) -> Bool](./cfreadstreamsetproperty%28_,_,_%29.md)
  Sets the value of a property for a stream.
### Getting the CFReadStream Type ID
- [func CFReadStreamGetTypeID() -> CFTypeID](./cfreadstreamgettypeid%28%29.md)
  Returns the type identifier the `CFReadStream` opaque type.
### Callbacks
- [typealias CFReadStreamClientCallBack](./cfreadstreamclientcallback.md)
  Callback invoked when certain types of activity takes place on a readable stream.
### Data Types
- [struct CFStreamClientContext](./cfstreamclientcontext.md)
  A structure that contains program-defined data and callbacks with which you can configure a stream’s client behavior.

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

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfreadstream)*