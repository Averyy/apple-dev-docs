# getControlPoint(at:values:)

**Framework**: Core Animation  
**Kind**: method

Returns the control point for the specified index.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func getControlPoint(at idx: Int, values ptr: UnsafeMutablePointer<Float>)
```

#### Discussion

The value of `index` must be between 0 and 3.

## Parameters

- `idx`: An integer specifying the index of the control point to return.
- `ptr`: A pointer to an array that, upon return, will contain the x and y values of the specified point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/camediatimingfunction/getcontrolpoint(at:values:))*