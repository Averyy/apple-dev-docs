# RPBroadcastActivityViewControllerDelegate

**Framework**: ReplayKit  
**Kind**: protocol  
**Role**: Protocol

The protocol you implement to respond to changes to a broadcast activity user interface.

**Availability**:
- iOS 10.0+ - Deprecated in 27.0
- iPadOS 10.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- tvOS 10.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0

> **Deprecated**: No longer supported

## Declaration

```swift
protocol RPBroadcastActivityViewControllerDelegate : NSObjectProtocol
```

```objc
@protocol RPBroadcastActivityViewControllerDelegate <NSObject>
```

## Overview

Use this class to respond to changes to a broadcast activity user interface, represented by an [`RPBroadcastActivityViewController`](./rpbroadcastactivityviewcontroller.md) object.

## Topics

### Connecting to a Service
- [func broadcastActivityViewController(RPBroadcastActivityViewController, didFinishWith: RPBroadcastController?, error: (any Error)?)](./rpbroadcastactivityviewcontrollerdelegate/broadcastactivityviewcontroller%28_,didfinishwith,error%29.md)
  Indicates that the broadcast activity view controller is ready to be dismissed.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Getting the Delegate
- [var delegate: (any RPBroadcastActivityViewControllerDelegate)?](./rpbroadcastactivityviewcontroller/delegate.md)
  The delegate for the broadcast activity view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/replaykit/rpbroadcastactivityviewcontrollerdelegate)*