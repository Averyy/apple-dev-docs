# ARSessionProviding

**Framework**: ARKit  
**Kind**: protocol  
**Role**: Protocol

An object that provides a session.

**Availability**:
- iOS
- iPadOS
- visionOS 1.0+ - Deprecated in 1.0

## Declaration

```swift
protocol ARSessionProviding : NSObjectProtocol
```

```objc
@protocol ARSessionProviding <NSObject>
```

#### Overview

As an example usage, [`ARCoachingOverlayView`](./arcoachingoverlayview.md) exposes [`sessionProvider`](./arcoachingoverlayview/sessionprovider.md) to access your app’s current session.

## Topics

### Providing a Session
- [var session: ARSession](./arsessionproviding/session.md)
  A contract to declare an AR session.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
### Conforming Types
- [ARSCNView](./arscnview.md)
- [ARSKView](./arskview.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arsessionproviding)*