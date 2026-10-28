# referenceObject

**Framework**: ARKit  
**Kind**: property  
**Role**: Instance Property

The detected object referenced by the object anchor.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+

## Declaration

```swift
var referenceObject: ARReferenceObject { get }
```

```objc
@property (nonatomic, strong, readonly) ARReferenceObject * referenceObject;
```

## Discussion

This object is always one of the [`ARReferenceObject`](../arreferenceobject.md) objects you provided in the [`detectionObjects`](../arworldtrackingconfiguration/detectionobjects.md) array when configuring the session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arobjectanchor/referenceobject)*