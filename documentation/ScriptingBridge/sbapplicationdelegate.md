# SBApplicationDelegate

**Framework**: Scripting Bridge  
**Kind**: protocol

This informal protocol defines a delegation method for handling Apple event errors that are sent from a target application to an [`SBApplication`](SBApplication.md) object.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.5+

## Declaration

```swift
protocol SBApplicationDelegate
```

#### Overview

You must set a delegate for the [`SBApplication`](sbapplication.md) object using the [`delegate`](sbapplication/delegate.md) method. If you do not set a delegate and have the delegate handle the error in some way, [`SBApplication`](sbapplication.md) raises an exception.

## Topics

### Handling Errors
- [func eventDidFail(UnsafePointer<AppleEvent>, withError: any Error) -> Any?](sbapplicationdelegate/eventdidfail(_:witherror:).md)
  Sent by an `SBApplication` object when a target application returns an error Apple event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scriptingbridge/sbapplicationdelegate)*