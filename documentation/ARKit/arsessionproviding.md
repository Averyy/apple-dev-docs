# ARSessionProviding

**Framework**: ARKit  
**Kind**: protocol

An object that provides a session.

## Declaration

```swift
protocol ARSessionProviding : NSObjectProtocol
```

#### Overview

As an example usage, [`ARCoachingOverlayView`](arcoachingoverlayview.md) exposes [`sessionProvider`](arcoachingoverlayview/sessionprovider.md) to access your app’s current session.

## Topics

### Providing a Session
- [var session: ARSession](arsessionproviding/session.md)
  A contract to declare an AR session.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Conforming Types
- [ARSCNView](arscnview.md)
- [ARSKView](arskview.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arsessionproviding)*