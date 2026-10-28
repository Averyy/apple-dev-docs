# SBApplication

**Framework**: Scripting Bridge  
**Kind**: class  
**Role**: Class

The `SBApplication` class provides a mechanism enabling an Objective-C program to send Apple events to a scriptable application and receive Apple events in response. It thereby makes it possible for that program to control the application and exchange data with it. Scripting Bridge works by bridging data types between Apple event descriptors and Cocoa objects.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.5+

## Declaration

```swift
class SBApplication
```

```objc
@interface SBApplication : SBObject
```

## Overview

Although `SBApplication` includes methods that manually send and process Apple events, you should never have to call these methods directly. Instead, subclasses of `SBApplication` implement application-specific methods that handle the sending of Apple events automatically.

For example, if you wanted to get the current iTunes track, you can simply use the `currentTrack` method of the dynamically defined subclass for the iTunes application—which handles the details of sending the Apple event for you—rather than figuring out the more complicated, low-level alternative:

```objc
[iTunes propertyWithCode:'pTrk'];
```

If you do need to send Apple events manually, consider using the `NSAppleEventDescriptor` class.

## Subclassing Notes

You rarely instantiate `SBApplication` objects directly. Instead, you get the shared instance of a application-specific subclass typically by calling one of the `applicationWith...` class methods, using a bundle identifier, process identifier, or URL to identify the application.

## Topics

### Initializing a Scriptable Application Object
- [init?(bundleIdentifier: String)](./sbapplication/init%28bundleidentifier%29.md)
  Returns an instance of an `SBApplication` subclass that represents the target application identified by the given bundle identifier.
- [init?(processIdentifier: pid_t)](./sbapplication/init%28processidentifier%29.md)
  Returns an instance of an `SBApplication` subclass that represents the target application identified by the given process identifier.
- [init?(url: URL)](./sbapplication/init%28url%29-6xbe5.md)
  Returns an instance of an `SBApplication` subclass that represents the target application identified by the given URL.
### Creating a Scripting Class
- [func `class`(forScriptingClass: String) -> AnyClass?](./sbapplication/class%28forscriptingclass%29.md)
  Returns a class object that represents a particular class in the target application.
### Controlling the Application
- [func activate()](./sbapplication/activate%28%29.md)
  Moves the target application to the foreground immediately.
- [var isRunning: Bool](./sbapplication/isrunning.md)
  A Boolean that indicates whether the target application represented by the receiver is running.
- [var launchFlags: LSLaunchFlags](./sbapplication/launchflags.md)
  The launch flags for the application represented by the receiver.
- [var sendMode: AESendMode](./sbapplication/sendmode.md)
  The mode for sending Apple events to the target application.
- [var timeout: Int](./sbapplication/timeout.md)
  The period the application will wait to receive reply Apple events.
### Managing the Delegate
- [var delegate: (any SBApplicationDelegate)?](./sbapplication/delegate.md)
  The error-handling delegate of the receiver.
### Initializers
- [init?(URL: URL)](./sbapplication/init%28url%29-2kr06.md)
- [init?(URL: URL)](./sbapplication/init%28url%29-4bno1.md)
### Getting a Scriptable Application Instance
- [+ applicationWithBundleIdentifier:](./sbapplication/applicationwithbundleidentifier_.md)
  Returns the shared instance representing the target application specified by its bundle identifier.
- [+ applicationWithProcessIdentifier:](./sbapplication/applicationwithprocessidentifier_.md)
  Returns the shared instance representing a target application specified by its process identifier.
- [+ applicationWithURL:](./sbapplication/applicationwithurl_.md)
  Returns the shared instance representing a target application specified by the given URL.

## Relationships

### Inherits From
- [SBObject](./sbobject.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/scriptingbridge/sbapplication)*