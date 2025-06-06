# Object Runtime

**Framework**: Foundation

Get low-level support for basic Objective-C features, Cocoa design patterns, and Swift integration.

## Topics

### Object Basics
- [class NSObject](../ObjectiveC/NSObject-swift.class.md)
  The root class of most Objective-C class hierarchies, from which subclasses inherit a basic interface to the runtime system and the ability to behave as Objective-C objects.
- [protocol NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
  The group of methods that are fundamental to all Objective-C objects.
- [NSKeyValueCoding](../ObjectiveC/nskeyvaluecoding.md)
  A mechanism by which you can access the properties of an object indirectly by name or key.
### Copying
- [protocol NSCopying](nscopying.md)
  A protocol that objects adopt to provide functional copies of themselves.
- [protocol NSMutableCopying](nsmutablecopying.md)
  A protocol that mutable objects adopt to provide functional copies of themselves.
### Value Wrappers and Transformations
- [class NSNumber](nsnumber.md)
  An object wrapper for primitive scalar numeric values.
- [class NSValue](nsvalue.md)
  A simple container for a single C or Objective-C data item.
- [class ValueTransformer](valuetransformer.md)
  An abstract class used to transform values from one representation to another.
### Swift Support
- [protocol ReferenceConvertible](referenceconvertible.md)
  A decoration applied to types that are backed by a Foundation reference type.
- [Classes Bridged to Swift Standard Library Value Types](classes-bridged-to-swift-standard-library-value-types.md)
  Use bridged reference types when you need reference semantics or Foundation-specific behavior.
### Remote Objects
- [class NSProxy](nsproxy.md)
  An abstract superclass defining an API for objects that act as stand-ins for other objects or for objects that don’t exist yet.
### Memory Management
- [Memory Management Functions](memory-management-functions.md)
  Perform low-level memory management tasks.
### Objective-C Runtime
- [Objective-C Runtime Utilities](objective-c-runtime-utilities.md)
  Interact with the Objective-C runtime.
### Versions and API Availability
- [Foundation Framework Version Numbers](foundation-framework-version-numbers.md)
  Recognize the constants for comparing the current running version of Foundation against known OS version numbers.
### Legacy
- [Distributed Objects Support](distributed-objects-support.md)
  Enable communication among objects in different processes, both locally and on remote systems.
- [Objective-C Garbage Collection](objective-c-garbage-collection.md)
  Interface with the legacy garbage collection system.

## See Also

- [XPC](xpc.md)
  Manage secure interprocess communication.
- [Processes and Threads](processes-and-threads.md)
  Manage your app’s interaction with the host operating system and other processes, and implement low-level concurrency features.
- [Streams, Sockets, and Ports](streams-sockets-and-ports.md)
  Use low-level Unix features to manage input and output among files, processes, and the network.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/object-runtime)*