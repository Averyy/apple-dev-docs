# NSAutoreleasePool

**Framework**: Foundation  
**Kind**: class  
**Role**: Class

An object that supports Cocoa’s reference-counted memory management system.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```objc
@interface NSAutoreleasePool : NSObject
```

#### Overview

An autorelease pool stores objects that are sent a `release` message when the pool itself is drained.

> ❗ **Important**:  If you use Automatic Reference Counting (ARC), you cannot use autorelease pools directly. Instead, you use `@autoreleasepool` blocks. For example, in place of:
>
> ```objc
> NSAutoreleasePool *pool = [[NSAutoreleasePool alloc] init];
> // Code benefitting from a local autorelease pool.
> [pool release];
> ```
>
> you would write:
>
> ```objc
> @autoreleasepool {
>    // Code benefitting from a local autorelease pool.
> }
> ```
>
> `@autoreleasepool` blocks are more efficient than using an instance of [`NSAutoreleasePool`](./nsautoreleasepool.md) directly; you can also use them even if you do not use ARC.

In a reference-counted environment (as opposed to one which uses garbage collection), an [`NSAutoreleasePool`](./nsautoreleasepool.md) object contains objects that have received an [`autorelease`](../ObjectiveC/nsobject-c.protocol/autorelease.md) message and when drained it sends a [`release`](../ObjectiveC/nsobject-c.protocol/release.md) message to each of those objects. Thus, sending [`autorelease`](../ObjectiveC/nsobject-c.protocol/autorelease.md) instead of [`release`](../ObjectiveC/nsobject-c.protocol/release.md) to an object extends the lifetime of that object at least until the pool itself is drained (it may be longer if the object is subsequently retained). An object can be put into the same pool several times, in which case it receives a [`release`](../ObjectiveC/nsobject-c.protocol/release.md) message for each time it was put into the pool.

In a reference counted environment, Cocoa expects there to be an autorelease pool always available. If a pool is not available, autoreleased objects do not get released and you leak memory. In this situation, your program will typically log suitable warning messages.

The Application Kit creates an autorelease pool on the main thread at the beginning of every cycle of the event loop, and drains it at the end, thereby releasing any autoreleased objects generated while processing an event. If you use the Application Kit, you therefore typically don’t have to create your own pools. If your application creates a lot of temporary autoreleased objects within the event loop, however, it may be beneficial to create “local” autorelease pools to help to minimize the peak memory footprint.

You create an [`NSAutoreleasePool`](./nsautoreleasepool.md) object with the usual `alloc` and `init` messages and dispose of it with [`drain`](./nsautoreleasepool/drain.md) (or `release`—to understand the difference, see [Garbage Collection](./nsautoreleasepool.md#Garbage-Collection)). Since you cannot retain an autorelease pool (or autorelease it—see `retain` and `autorelease`), draining a pool ultimately has the effect of deallocating it. You should always drain an autorelease pool in the same context (invocation of a method or function, or body of a loop) that it was created. See [Using Autorelease Pool Blocks](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/MemoryMgmt/Articles/mmAutoreleasePools.html#//apple_ref/doc/uid/20000047) for more details.

Each thread (including the main thread) maintains its own stack of [`NSAutoreleasePool`](./nsautoreleasepool.md) objects (see [Threads](./nsautoreleasepool.md#Threads)). As new pools are created, they get added to the top of the stack. When pools are deallocated, they are removed from the stack. Autoreleased objects are placed into the top autorelease pool for the current thread. When a thread terminates, it automatically drains all of the autorelease pools associated with itself.

##### Threads

If you are making Cocoa calls outside of the Application Kit’s main thread—for example if you create a Foundation-only application or if you detach a thread—you need to create your own autorelease pool.

If your application or thread is long-lived and potentially generates a lot of autoreleased objects, you should periodically drain and create autorelease pools (like the Application Kit does on the main thread); otherwise, autoreleased objects accumulate and your memory footprint grows. If, however, your detached thread does not make Cocoa calls, you do not need to create an autorelease pool.

> **Note**:  If you are creating secondary threads using the POSIX thread APIs instead of `NSThread` objects, you cannot use Cocoa, including `NSAutoreleasePool`, unless Cocoa is in multithreading mode. Cocoa enters multithreading mode only after detaching its first `NSThread` object. To use Cocoa on secondary POSIX threads, your application must first detach at least one `NSThread` object, which can immediately exit. You can test whether Cocoa is in multithreading mode with the `NSThread` class method [`isMultiThreaded()`](./thread/ismultithreaded%28%29.md).

##### Garbage Collection

In a garbage-collected environment, there is no need for autorelease pools. You may, however, write a framework that is designed to work in both a garbage-collected and reference-counted environment. In this case, you can use autorelease pools to hint to the collector that collection may be appropriate. In a garbage-collected environment, sending a [`drain`](./nsautoreleasepool/drain.md) message to a pool triggers garbage collection if necessary; `release`, however, is a no-op. In a reference-counted environment, [`drain`](./nsautoreleasepool/drain.md) has the same effect as `release`. Typically, therefore, you should use [`drain`](./nsautoreleasepool/drain.md) instead of `release`.

## Topics

### Managing a Pool
- [- drain](./nsautoreleasepool/drain.md)
  In a reference-counted environment, releases and pops the receiver; in a garbage-collected environment, triggers garbage collection if the memory allocated since the last collection is greater than the current threshold.
### Adding an Object to a Pool
- [+ addObject:](./nsautoreleasepool/addobject_-c.type.method.md)
  Adds a given object to the active autorelease pool in the current thread.
- [- addObject:](./nsautoreleasepool/addobject_-c.method.md)
  Adds a given object to the receiver
### Debugging
- [+ showPools](./nsautoreleasepool/showpools.md)
  Displays the state of the current thread’s autorelease pool stack to `stderr`.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)

## See Also

### Memory Management
- [Memory Management Functions](./memory-management-functions.md)
  Perform low-level memory management tasks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsautoreleasepool)*