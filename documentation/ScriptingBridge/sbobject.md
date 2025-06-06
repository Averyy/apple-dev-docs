# SBObject

**Framework**: Scripting Bridge  
**Kind**: class

The `SBObject` class declares methods that can be invoked on any object in a scriptable application. It defines methods for getting elements and properties of an object, as well as setting a given object to a new value.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.5+

## Declaration

```swift
class SBObject
```

#### Overview

Each `SBObject` is built around an object specifier, which tells Scripting Bridge how to locate the object. Therefore, you can think of an `SBObject` as a reference to an object in an target application rather than an object itself. To bypass this reference-based approach and force evaluation, use the [`get()`](sbobject/get().md) method.

Typically, rather than create `SBObject` instances explictly, you receive `SBObject` objects by calling methods of an [`SBApplication`](sbapplication.md) subclass. For example, if you wanted to get an `SBObject` representing the current iTunes track, you would use code like this (where `iTunesTrack` is a subclass of `SBObject`):

```objc
iTunesApplication *iTunes = [SBApplication applicationWithBundleIdentifier:@"com.apple.iTunes"];
iTunesTrack *track = [iTunes currentTrack];
```

You can discover the names of dynamically generated classes such as `iTunesApplication` and `iTunesTrack` by examining the header file created by the `sdp` tool. Alternatively, you give these variables the dynamic Objective-C type `id`.

## Topics

### Initializing a Scripting Bridge Object
- [init()](sbobject/init.md)
  Initializes and returns an instance of an `SBObject` subclass.
- [init(data: Any)](sbobject/init(data:).md)
  Returns an instance of an `SBObject` subclass initialized with the given data.
- [init(properties: [AnyHashable : Any])](sbobject/init(properties:).md)
  Returns an instance of an `SBObject` subclass initialized with the specified properties.
- [init(elementCode: DescType, properties: [String : Any]?, data: Any?)](sbobject/init(elementcode:properties:data:).md)
  Returns an instance of an `SBObject` subclass initialized with the specified properties and data and added to the designated element array.
### Getting Referenced Data
- [func get() -> Any?](sbobject/get.md)
  Forces evaluation of the receiver, causing the real object to be returned immediately.
### Sending Apple Events
- [func setTo(Any?)](sbobject/setto(_:).md)
  Sets the receiver to a specified value.
### Getting Properties and Elements
- [func property(with: AnyClass, code: AEKeyword) -> SBObject](sbobject/property(with:code:).md)
  Returns an object of the designated scripting class representing the specified property of the receiver
- [func property(withCode: AEKeyword) -> SBObject](sbobject/property(withcode:).md)
  Returns an object representing the specified property of the receiver.
- [func elementArray(withCode: DescType) -> SBElementArray](sbobject/elementarray(withcode:).md)
  Returns an array containing every child of the receiver with the given class-type code.
### Instance Methods
- [func lastError() -> (any Error)?](sbobject/lasterror.md)
  The error from the last event this object sent, or nil if it succeeded.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [SBApplication](sbapplication.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/scriptingbridge/sbobject)*