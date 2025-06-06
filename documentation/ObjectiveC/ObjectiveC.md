# Objective-C Runtime

**Framework**: Objective-C Runtime  
**Kind**: module

Gain low-level access to the Objective-C runtime and the Objective-C root types.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

#### Overview

The [`Objective-C Runtime`](ObjectiveC.md) module APIs define the base of the Objective-C language. These APIs include:

- Types such as the [`NSObject`](nsobject-swift.class.md) class and the [`NSObjectProtocol`](nsobjectprotocol.md) protocol that provide the root functionality of most Objective-C classes
- Functions and data structures that comprise the Objective-C runtime, which provides support for the dynamic properties of the Objective-C language

You typically don’t need to use this module directly.

## Topics

### Classes
- [class NSObject](nsobject-swift.class.md)
  The root class of most Objective-C class hierarchies, from which subclasses inherit a basic interface to the runtime system and the ability to behave as Objective-C objects.
- [class Protocol](protocol.md)
### Protocols
- [protocol NSObjectProtocol](nsobjectprotocol.md)
  The group of methods that are fundamental to all Objective-C objects.
### Reference
- [Objective-C Runtime](objective-c-runtime.md)
  Describes the macOS Objective-C runtime library support functions and data structures.
- [Objective-C Structures](objective-c-structures.md)
- [Objective-C Constants](objective-c-constants.md)
- [Objective-C Functions](objective-c-functions.md)
- [Objective-C Data Types](objective-c-data-types.md)
- [Objective-C Macros](objective-c-macros.md)
- [Objective-C Enumerations](objective-c-enums.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/ObjectiveC)*