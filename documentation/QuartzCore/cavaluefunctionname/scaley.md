# scaleY

**Framework**: Core Animation  
**Kind**: property  
**Role**: Type Property

A value function scales by the input value along the y-axis. Animations referencing this value function must provide a single animation value.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
static let scaleY: CAValueFunctionName
```

```c
extern CAValueFunctionName const kCAValueFunctionScaleY;
```

## See Also

### Constants
- [static let scale: CAValueFunctionName](./scale.md)
  A value function scales by the input value along all three axis. Animations using this value transform function must provide animation values in an `NSArray` of three `NSNumber` instances that specify the (x, y, z) scale values.
- [static let scaleX: CAValueFunctionName](./scalex.md)
  A value function scales by the input value along the x-axis. Animations referencing this value transform function must provide a single animation value.
- [static let scaleZ: CAValueFunctionName](./scalez.md)
  A value function that scales by the input value along the z-axis. Animations referencing this value function must provide a single animation value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/cavaluefunctionname/scaley)*