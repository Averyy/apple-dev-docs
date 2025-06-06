# Translate Functions

**Framework**: Core Animation

Translate value transform functions construct a 4x4 matrix that represents the corresponding translate matrix.

## Topics

### Constants
- [static let translate: CAValueFunctionName](cavaluefunctionname/translate.md)
  A value function that translates by the input values along all three axis. Animations using this value transform function must provide animation values in an `NSArray` of three `NSNumber` instances that specify the (x, y, z) translate values.
- [static let translateX: CAValueFunctionName](cavaluefunctionname/translatex.md)
  A value function translates by the input value along the x-axis. Animations referencing this value function must provide a single input value.
- [static let translateY: CAValueFunctionName](cavaluefunctionname/translatey.md)
  A value function translates by the input value along the y-axis. Animations referencing this value function must provide a single input value.
- [static let translateZ: CAValueFunctionName](cavaluefunctionname/translatez.md)
  A value function translates by the input value along the z-axis. Animations referencing this value function must provide a single input value.

## See Also

- [Rotate Value Functions](rotate-value-functions.md)
  Rotate value transform functions construct a 4x4 matrix that represents the corresponding rotation matrix.
- [Scale Value Functions](scale-value-functions.md)
  Scale value transform functions construct a 4x4 matrix that represents the corresponding scale matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/translate-functions)*