# supportedNumberOfTrackedFaces

**Framework**: ARKit  
**Kind**: property  
**Role**: Type Property

The maximum number of faces that the framework can track.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+

## Declaration

```swift
class var supportedNumberOfTrackedFaces: Int { get }
```

```objc
@property (class, nonatomic, readonly) NSInteger supportedNumberOfTrackedFaces;
```

#### Discussion

Do not exceed this value when you set [`maximumNumberOfTrackedFaces`](./maximumnumberoftrackedfaces.md).

## See Also

### Tracking Multiple Faces
- [var maximumNumberOfTrackedFaces: Int](./maximumnumberoftrackedfaces.md)
  The number of faces to track during the session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arfacetrackingconfiguration/supportednumberoftrackedfaces)*