# CFWriteStream

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
class CFWriteStream
```

#### Overview

`CFWriteStream` provides an interface for writing a byte stream either synchronously or asynchronously. You can create streams that write bytes to a block of memory, a file, or a generic socket. All streams need to be opened, using [`CFWriteStreamOpen(_:)`](cfwritestreamopen(_:).md), before writing.

Use [`CFReadStream`](cfreadstream.md) for reading byte streams, and for the functions, such as [`CFStreamCreatePairWithSocketToHost(_:_:_:_:_:)`](cfstreamcreatepairwithsockettohost(_:_:_:_:_:).md), that create socket streams).

`CFWriteStream` is “toll-free bridged” with its Cocoa Foundation counterpart, [`OutputStream`](https://developer.apple.com/documentation/Foundation/OutputStream). This means that the Core Foundation type is interchangeable in function or method calls with the bridged Foundation object. Therefore, in a method where you see an `NSOutputStream *` parameter, you can pass in a `CFWriteStreamRef`, and in a function where you see a `CFWriteStreamRef` parameter, you can pass in an `NSOutputStream` instance. Note, however, that you may have either a delegate or callbacks but not both. See [`Toll-Free Bridged Types`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFDesignConcepts/Articles/tollFreeBridgedTypes.html#//apple_ref/doc/uid/TP40010677) for more information on toll-free bridging.

## Topics

### Creating a Write Stream
- [func CFWriteStreamCreateWithAllocatedBuffers(CFAllocator!, CFAllocator!) -> CFWriteStream!](cfwritestreamcreatewithallocatedbuffers(_:_:).md)
  Creates a writable stream for a growable block of memory.
- [func CFWriteStreamCreateWithBuffer(CFAllocator!, UnsafeMutablePointer<UInt8>!, CFIndex) -> CFWriteStream!](cfwritestreamcreatewithbuffer(_:_:_:).md)
  Creates a writable stream for a fixed-size block of memory.
- [func CFWriteStreamCreateWithFile(CFAllocator!, CFURL!) -> CFWriteStream!](cfwritestreamcreatewithfile(_:_:).md)
  Creates a writable stream for a file.
### Opening and Closing a Stream
- [func CFWriteStreamClose(CFWriteStream!)](cfwritestreamclose(_:).md)
  Closes a writable stream.
- [func CFWriteStreamOpen(CFWriteStream!) -> Bool](cfwritestreamopen(_:).md)
  Opens a stream for writing.
### Writing to a Stream
- [func CFWriteStreamWrite(CFWriteStream!, UnsafePointer<UInt8>!, CFIndex) -> CFIndex](cfwritestreamwrite(_:_:_:).md)
  Writes data to a writable stream.
### Scheduling a Write Stream
- [func CFWriteStreamScheduleWithRunLoop(CFWriteStream!, CFRunLoop!, CFRunLoopMode!)](cfwritestreamschedulewithrunloop(_:_:_:).md)
  Schedules a stream into a run loop.
- [func CFWriteStreamUnscheduleFromRunLoop(CFWriteStream!, CFRunLoop!, CFRunLoopMode!)](cfwritestreamunschedulefromrunloop(_:_:_:).md)
  Removes a stream from a particular run loop.
### Examining Stream Properties
- [func CFWriteStreamCanAcceptBytes(CFWriteStream!) -> Bool](cfwritestreamcanacceptbytes(_:).md)
  Returns whether a writable stream can accept new data without blocking.
- [func CFWriteStreamCopyProperty(CFWriteStream!, CFStreamPropertyKey!) -> CFTypeRef!](cfwritestreamcopyproperty(_:_:).md)
  Returns the value of a property for a stream.
- [func CFWriteStreamCopyError(CFWriteStream!) -> CFError!](cfwritestreamcopyerror(_:).md)
  Returns the error associated with a stream.
- [func CFWriteStreamGetError(CFWriteStream!) -> CFStreamError](cfwritestreamgeterror(_:).md)
  Returns the error status of a stream.
- [func CFWriteStreamGetStatus(CFWriteStream!) -> CFStreamStatus](cfwritestreamgetstatus(_:).md)
  Returns the current state of a stream.
### Setting Stream Properties
- [func CFWriteStreamSetClient(CFWriteStream!, CFOptionFlags, CFWriteStreamClientCallBack!, UnsafeMutablePointer<CFStreamClientContext>!) -> Bool](cfwritestreamsetclient(_:_:_:_:).md)
  Assigns a client to a stream, which receives callbacks when certain events occur.
- [func CFWriteStreamSetProperty(CFWriteStream!, CFStreamPropertyKey!, CFTypeRef!) -> Bool](cfwritestreamsetproperty(_:_:_:).md)
  Sets the value of a property for a stream.
### Getting the CFWriteStream Type ID
- [func CFWriteStreamGetTypeID() -> CFTypeID](cfwritestreamgettypeid().md)
  Returns the type identifier of all CFWriteStream objects.
### Callbacks
- [typealias CFWriteStreamClientCallBack](cfwritestreamclientcallback.md)
  Callback invoked when certain types of activity takes place on a writable stream.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

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

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfwritestream)*