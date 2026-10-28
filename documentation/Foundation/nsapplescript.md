# NSAppleScript

**Framework**: Foundation  
**Kind**: class  
**Role**: Class

An object that provides the ability to load, compile, and execute scripts.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
class NSAppleScript
```

```objc
@interface NSAppleScript : NSObject
```

## Overview

This class provides applications with the ability to

- load a script from a URL or from a text string
- compile or execute a script or an individual Apple event
- obtain an `NSAppleEventDescriptor` containing the reply from an executed script or event
- obtain an attributed string for a compiled script, suitable for display in a script editor
- obtain various kinds of information about any errors that may occur

> ❗ **Important**:  `NSAppleScript` provides the [`executeAppleEvent(_:error:)`](./nsapplescript/executeappleevent%28_,error%29.md) method so that you can send an Apple event to invoke a handler in a script. (In an AppleScript script, a handler is the equivalent of a function.) However, you cannot use this method to send Apple events to other applications.

When you create an instance of `NSAppleScript` object, you can use a URL to specify a script that can be in either text or compiled form, or you can supply the script as a string. Should an error occur when compiling or executing the script, several of the methods return a dictionary containing error information. The keys for obtaining error information, such as [`errorMessage`](./nsapplescript/errormessage.md), are described in the Constants section.

See also NSAppleScript Additions Reference in the Application Kit framework, which defines a method that returns the syntax-highlighted source code for a script.

## Topics

### Initializing a Script
- [init?(contentsOf: URL, error: AutoreleasingUnsafeMutablePointer<NSDictionary?>?)](./nsapplescript/init%28contentsof,error%29.md)
  Initializes a newly allocated script instance from the source identified by the passed URL.
- [init?(source: String)](./nsapplescript/init%28source%29.md)
  Initializes a newly allocated script instance from the passed source.
### Getting Information About a Script
- [var isCompiled: Bool](./nsapplescript/iscompiled.md)
  A Boolean value that indicates whether the receiver’s script has been compiled.
- [var source: String?](./nsapplescript/source.md)
  The script source for the receiver.
### Compiling and Executing a Script
- [func compileAndReturnError(AutoreleasingUnsafeMutablePointer<NSDictionary?>?) -> Bool](./nsapplescript/compileandreturnerror%28_%29.md)
  Compiles the receiver, if it is not already compiled.
- [func executeAndReturnError(AutoreleasingUnsafeMutablePointer<NSDictionary?>?) -> NSAppleEventDescriptor](./nsapplescript/executeandreturnerror%28_%29.md)
  Executes the receiver, compiling it first if it is not already compiled.
- [func executeAppleEvent(NSAppleEventDescriptor, error: AutoreleasingUnsafeMutablePointer<NSDictionary?>?) -> NSAppleEventDescriptor](./nsapplescript/executeappleevent%28_,error%29.md)
  Executes an Apple event in the context of the receiver, as a means of allowing the application to invoke a handler in the script.
### Constants
- [Error Dictionary Keys](./error-dictionary-keys.md)
  If the result of [`init(contentsOf:error:)`](./nsapplescript/init%28contentsof,error%29.md), [`compileAndReturnError(_:)`](./nsapplescript/compileandreturnerror%28_%29.md), [`executeAndReturnError(_:)`](./nsapplescript/executeandreturnerror%28_%29.md), or [`executeAppleEvent(_:error:)`](./nsapplescript/executeappleevent%28_,error%29.md), signals failure (`nil`, [`false`](../Swift/false.md), `nil`, or `nil`, respectively), a pointer to an autoreleased dictionary is put at the location pointed to by the error parameter. The error info dictionary may contain entries that use any combination of the following keys, including no entries at all.
### Instance Properties
- [var richTextSource: NSAttributedString?](./nsapplescript/richtextsource.md)
  Returns the syntax-highlighted source code of the receiver if the receiver has been compiled and its source code is available.
### Initializers
- [init?(contentsOfURL: URL, error: AutoreleasingUnsafeMutablePointer<NSDictionary?>?)](./nsapplescript/init%28contentsofurl,error%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](./nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsapplescript)*