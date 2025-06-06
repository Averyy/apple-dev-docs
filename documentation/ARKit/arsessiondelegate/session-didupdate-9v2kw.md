# session(_:didUpdate:)

**Framework**: ARKit  
**Kind**: method

Provides a newly captured camera image and accompanying AR information to the delegate.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
optional func session(_ session: ARSession, didUpdate frame: ARFrame)
```

## Mentions

- [Displaying an AR Experience with Metal](displaying-an-ar-experience-with-metal.md)

#### Discussion

Implement this method if you provide your own display for rendering an AR experience. The provided [`ARFrame`](arframe.md) object contains the latest image captured from the device camera, which you can render as a scene background, as well as information about camera parameters and anchor transforms you can use for rendering virtual content on top of the camera image.

## Parameters

- `session`: The session providing information.
- `frame`: An object containing the new camera image and AR information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arsessiondelegate/session(_:didupdate:)-9v2kw)*