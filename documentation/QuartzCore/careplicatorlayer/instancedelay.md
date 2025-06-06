# instanceDelay

**Framework**: Core Animation  
**Kind**: property

Specifies the delay, in seconds, between replicated copies. Animatable.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var instanceDelay: CFTimeInterval { get set }
```

#### Discussion

The default value is `0.0`, meaning that any animations added to replicated copies will be synchronized.

The following code shows a replicator layer being used to create an animated activity monitor. The replicator layer creates 30 small circles forming a larger circle. The source layer, `circle`, has a 1 second animated fade out and each of the copies offsets the time of the animation by 1 / 30 seconds.

```swift
let replicatorLayer = CAReplicatorLayer()
     
let circle = CALayer()
circle.frame = CGRect(origin: CGPoint.zero,
                      size: CGSize(width: 10, height: 10))
circle.backgroundColor = NSColor.blue.cgColor
circle.cornerRadius = 5
circle.position = CGPoint(x: 0, y: 50)
replicatorLayer.addSublayer(circle)
     
let fadeOut = CABasicAnimation(keyPath: "opacity")
fadeOut.fromValue = 1
fadeOut.toValue = 0
fadeOut.duration = 1
fadeOut.repeatCount = Float.greatestFiniteMagnitude
circle.add(fadeOut, forKey: nil)
     

let instanceCount = 30
replicatorLayer.instanceCount = instanceCount
replicatorLayer.instanceDelay = fadeOut.duration / CFTimeInterval(instanceCount)
     
let angle = -CGFloat.pi * 2 / CGFloat(instanceCount)
replicatorLayer.instanceTransform = CATransform3DMakeRotation(angle, 0, 0, 1)
```

The following illustration shows the result of the above code:

![Activity monitor created with a replicator layer.](https://docs-assets.developer.apple.com/published/0b5763d877995b7dfa79b186f719ccf4/media-2776911%402x.png)

## See Also

- [var instanceCount: Int](careplicatorlayer/instancecount.md)
  The number of copies to create, including the source layers.
- [var instanceTransform: CATransform3D](careplicatorlayer/instancetransform.md)
  The transform matrix applied to the previous instance to produce the current instance. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/careplicatorlayer/instancedelay)*