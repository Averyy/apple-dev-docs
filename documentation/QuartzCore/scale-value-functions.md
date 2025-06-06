# Scale Value Functions

**Framework**: Core Animation

Scale value transform functions construct a 4x4 matrix that represents the corresponding scale matrix.

## Topics

### Constants
- [static let scale: CAValueFunctionName](cavaluefunctionname/scale.md)
  A value function scales by the input value along all three axis. Animations using this value transform function must provide animation values in an `NSArray` of three `NSNumber` instances that specify the (x, y, z) scale values.
- [static let scaleX: CAValueFunctionName](cavaluefunctionname/scalex.md)
  A value function scales by the input value along the x-axis. Animations referencing this value transform function must provide a single animation value.
- [static let scaleY: CAValueFunctionName](cavaluefunctionname/scaley.md)
  A value function scales by the input value along the y-axis. Animations referencing this value function must provide a single animation value.
- [static let scaleZ: CAValueFunctionName](cavaluefunctionname/scalez.md)
  A value function that scales by the input value along the z-axis. Animations referencing this value function must provide a single animation value.

## See Also

- [Rotate Value Functions](rotate-value-functions.md)
  Rotate value transform functions construct a 4x4 matrix that represents the corresponding rotation matrix.
- [Translate Functions](translate-functions.md)
  Translate value transform functions construct a 4x4 matrix that represents the corresponding translate matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/scale-value-functions)*