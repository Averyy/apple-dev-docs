# Scripting Bridge

**Framework**: Scripting Bridge  
**Kind**: module

Automate scriptable apps by sending and receiving Apple events.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.5+

#### Overview

Scripting Bridge is a technology that lets you control scriptable Apple and third-party applications using standard Objective-C syntax. Introduced in OS X version 10.5 (Leopard), the Scripting Bridge framework dynamically implements an Objective-C bridge to OSA-compliant applications—that is, applications having a scripting interface (usually defined in a `sdef` file). As part of this implementation, it generates Objective-C class implementations of the classes it finds in the scripting interface, including objects and methods representing properties, elements, commands, and so on. The objects are derived from classes defined in the Scripting Bridge framework.

## Topics

### Classes
- [class SBApplication](sbapplication.md)
  The `SBApplication` class provides a mechanism enabling an Objective-C program to send Apple events to a scriptable application and receive Apple events in response. It thereby makes it possible for that program to control the application and exchange data with it. Scripting Bridge works by bridging data types between Apple event descriptors and Cocoa objects.
- [class SBElementArray](sbelementarray.md)
  `SBElementArray` is subclass of `NSMutableArray` that manages collections of related [`SBObject`](sbobject.md) objects. For example, when you ask the Finder for a list of disks, or ask iTunes for a list of playlists, you get the result back as an `SBElementArray` containing Scripting Bridge objects representing those items.
- [class SBObject](sbobject.md)
  The `SBObject` class declares methods that can be invoked on any object in a scriptable application. It defines methods for getting elements and properties of an object, as well as setting a given object to a new value.
### Protocols
- [protocol SBApplicationDelegate](sbapplicationdelegate.md)
  This informal protocol defines a delegation method for handling Apple event errors that are sent from a target application to an [`SBApplication`](SBApplication.md) object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/ScriptingBridge)*