# CFFileDescriptor

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
class CFFileDescriptor
```

#### Overview

The CFFileDescriptor provides an opaque type to monitor file descriptors for read and write activity via CFRunLoop.

You use CFFileDescriptor to monitor file descriptors for read and write activity via CFRunLoop using callbacks. Each call back is one-shot, and must be re-enabled if you want to get another one.

You can re-enable the callback in the callback function itself, but you must completely service the file descriptor before doing so. For example, if you create a CFFileDescriptor for a pipe and get a callback because there are bytes to be read, then if you don’t read all of the bytes but nevertheless re-enable the CFFileDescriptor for read activity, you’ll get called back again immediately.

You can monitor kqueue file descriptors for read activity to find out when an event the kqueue is filtering for has occurred. You are responsible for understanding the use of the kevent() API and inserting and removing filters from the kqueue file descriptor yourself.

The following example takes a UNIX process ID as argument, and watches up to 20 seconds, and reports if the process terminates in that time:

```objc
// cc test.c -framework CoreFoundation -O
#include <CoreFoundation/CoreFoundation.h>
#include <unistd.h>
#include <sys/event.h>
static void noteProcDeath(CFFileDescriptorRef fdref, CFOptionFlags callBackTypes, void *info) {
    struct kevent kev;
    int fd = CFFileDescriptorGetNativeDescriptor(fdref);
    kevent(fd, NULL, 0, &kev, 1, NULL);
    // take action on death of process here
    printf("process with pid '%u' died\n", (unsigned int)kev.ident);
    CFFileDescriptorInvalidate(fdref);
    CFRelease(fdref); // the CFFileDescriptorRef is no longer of any use in this example
}
// one argument, an integer pid to watch, required
int main(int argc, char *argv[]) {
    if (argc < 2) exit(1);
    int fd = kqueue();
    struct kevent kev;
    EV_SET(&kev, atoi(argv[1]), EVFILT_PROC, EV_ADD|EV_ENABLE, NOTE_EXIT, 0, NULL);
    kevent(fd, &kev, 1, NULL, 0, NULL);
    CFFileDescriptorRef fdref = CFFileDescriptorCreate(kCFAllocatorDefault, fd, true, noteProcDeath, NULL);
    CFFileDescriptorEnableCallBacks(fdref, kCFFileDescriptorReadCallBack);
    CFRunLoopSourceRef source = CFFileDescriptorCreateRunLoopSource(kCFAllocatorDefault, fdref, 0);
    CFRunLoopAddSource(CFRunLoopGetMain(), source, kCFRunLoopDefaultMode);
    CFRelease(source);
    // run the run loop for 20 seconds
    CFRunLoopRunInMode(kCFRunLoopDefaultMode, 20.0, false);
    return 0;
}
```

## Topics

### Creating a CFFileDescriptor
- [func CFFileDescriptorCreate(CFAllocator!, CFFileDescriptorNativeDescriptor, Bool, CFFileDescriptorCallBack!, UnsafePointer<CFFileDescriptorContext>!) -> CFFileDescriptor!](cffiledescriptorcreate(_:_:_:_:_:).md)
  Creates a new CFFileDescriptor.
### Getting Information About a File Descriptor
- [func CFFileDescriptorGetNativeDescriptor(CFFileDescriptor!) -> CFFileDescriptorNativeDescriptor](cffiledescriptorgetnativedescriptor(_:).md)
  Returns the native file descriptor for a given CFFileDescriptor.
- [func CFFileDescriptorIsValid(CFFileDescriptor!) -> Bool](cffiledescriptorisvalid(_:).md)
  Returns a Boolean value that indicates whether the native file descriptor for a given CFFileDescriptor is valid.
- [func CFFileDescriptorGetContext(CFFileDescriptor!, UnsafeMutablePointer<CFFileDescriptorContext>!)](cffiledescriptorgetcontext(_:_:).md)
  Gets the context for a given CFFileDescriptor.
### Invalidating a File Descriptor
- [func CFFileDescriptorInvalidate(CFFileDescriptor!)](cffiledescriptorinvalidate(_:).md)
  Invalidates a CFFileDescriptor object.
### Managing Callbacks
- [func CFFileDescriptorEnableCallBacks(CFFileDescriptor!, CFOptionFlags)](cffiledescriptorenablecallbacks(_:_:).md)
  Enables callbacks for a given CFFileDescriptor.
- [func CFFileDescriptorDisableCallBacks(CFFileDescriptor!, CFOptionFlags)](cffiledescriptordisablecallbacks(_:_:).md)
  Disables callbacks for a given CFFileDescriptor.
### Creating a Run Loop Source
- [func CFFileDescriptorCreateRunLoopSource(CFAllocator!, CFFileDescriptor!, CFIndex) -> CFRunLoopSource!](cffiledescriptorcreaterunloopsource(_:_:_:).md)
  Creates a new runloop source for a given CFFileDescriptor.
### Getting the CFFileDescriptor Type ID
- [func CFFileDescriptorGetTypeID() -> CFTypeID](cffiledescriptorgettypeid().md)
  Returns the type identifier for the CFFileDescriptor opaque type.
### Data Types
- [typealias CFFileDescriptorNativeDescriptor](cffiledescriptornativedescriptor.md)
  Defines a type for the native file descriptor.
- [typealias CFFileDescriptorCallBack](cffiledescriptorcallback.md)
  Defines a structure for a callback for a CFFileDescriptor.
- [struct CFFileDescriptorContext](cffiledescriptorcontext.md)
  Defines a structure for the context of a CFFileDescriptor.
### Constants
- [Callback Identifiers](1477595-callback-identifiers.md)
  Constants that identify the read and write callbacks.

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

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cffiledescriptor)*