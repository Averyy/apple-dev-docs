# SBObject

**Framework**: Scripting Bridge  
**Kind**: class  
**Role**: Class

The `SBObject` class declares methods that can be invoked on any object in a scriptable application. It defines methods for getting elements and properties of an object, as well as setting a given object to a new value.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.5+

## Declaration

```swift
class SBObject
```

```objc
@interface SBObject : NSObject
```

#### Overview

Each `SBObject` is built around an object specifier, which tells Scripting Bridge how to locate the object. Therefore, you can think of an `SBObject` as a reference to an object in an target application rather than an object itself. To bypass this reference-based approach and force evaluation, use the [`get()`](./sbobject/get%28%29.md) method.

Typically, rather than create `SBObject` instances explictly, you receive `SBObject` objects by calling methods of an [`SBApplication`](./sbapplication.md) subclass. For example, if you wanted to get an `SBObject` representing the current iTunes track, you would use code like this (where `iTunesTrack` is a subclass of `SBObject`):

```objc
iTunesApplication *iTunes = [SBApplication applicationWithBundleIdentifier:@"com.apple.iTunes"];
iTunesTrack *track = [iTunes currentTrack];
```

You can discover the names of dynamically generated classes such as `iTunesApplication` and `iTunesTrack` by examining the header file created by the `sdp` tool. Alternatively, you give these variables the dynamic Objective-C type `id`.

## Topics

### Initializing a Scripting Bridge Object
- [init()](./sbobject/init%28%29.md)
  Initializes and returns an instance of an `SBObject` subclass.
- [init(data: Any)](./sbobject/init%28data%29.md)
  Returns an instance of an `SBObject` subclass initialized with the given data.
- [init(properties: [AnyHashable : Any])](./sbobject/init%28properties%29.md)
  Returns an instance of an `SBObject` subclass initialized with the specified properties.
- [init(elementCode: DescType, properties: [String : Any]?, data: Any?)](./sbobject/init%28elementcode,properties,data%29.md)
  Returns an instance of an `SBObject` subclass initialized with the specified properties and data and added to the designated element array.
### Getting Referenced Data
- [func get() -> Any?](./sbobject/get%28%29.md)
  Forces evaluation of the receiver, causing the real object to be returned immediately.
### Sending Apple Events
- [func setTo(Any?)](./sbobject/setto%28_%29.md)
  Sets the receiver to a specified value.
- [- sendEvent:id:parameters:](./sbobject/sendevent_id_parameters_.md)
  Sends an Apple event with the given event class, event ID, and format to the target application.
### Getting Properties and Elements
- [func property(with: AnyClass, code: AEKeyword) -> SBObject](./sbobject/property%28with,code%29.md)
  Returns an object of the designated scripting class representing the specified property of the receiver
- [func property(withCode: AEKeyword) -> SBObject](./sbobject/property%28withcode%29.md)
  Returns an object representing the specified property of the receiver.
- [func elementArray(withCode: DescType) -> SBElementArray](./sbobject/elementarray%28withcode%29.md)
  Returns an array containing every child of the receiver with the given class-type code.
### Initializers
- [init?(coder: NSCoder)](./sbobject/init%28coder%29.md)
### Instance Methods
- [func lastError() -> (any Error)?](./sbobject/lasterror%28%29.md)
  The error from the last event this object sent, or nil if it succeeded.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [SBApplication](./sbapplication.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/scriptingbridge/sbobject)*