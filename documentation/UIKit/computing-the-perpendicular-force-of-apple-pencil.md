# Computing the perpendicular force of Apple Pencil

**Framework**: UIKit

Adjust the force values reported by Apple Pencil so that they’re consistent with 3D Touch force values.

#### Overview

On a 3D Touch device, force from a person’s fingers is measured perpendicular to the surface of the screen. However, force reported by Apple Pencil is measured along its long axis, which often isn’t perpendicular to the screen. Instead of using the Apple Pencil force values as is, you might want to compute only the perpendicular portion of the force so that you can use the same code for touches originating from a person’s fingers or from Apple Pencil.

The following code shows how to add a `perpendicularForce` property to the [`UITouch`](uitouch.md) class to report the perpendicular force supplied by Apple Pencil. For touches involving Apple Pencil, this method divides the reported force value by the sine of the pencil’s altitude. For other touches, it reports the existing force value.

```swift
extension UITouch {
    var perpendicularForce: CGFloat {
        if type == .pencil {
            return force / sin(altitudeAngle)
        } else {
            return force
        }
    }
}

```


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/computing-the-perpendicular-force-of-apple-pencil)*