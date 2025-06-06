# init(name:)

**Framework**: Core Animation  
**Kind**: init

Creates and returns a new instance of `CAMediaTimingFunction` configured with the predefined timing function specified by `name`.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
convenience init(name: CAMediaTimingFunctionName)
```

#### Return Value

A new instance of `CAMediaTimingFunction` with the timing function specified by `name`.

## Parameters

- `name`: The timing function to use as specified in  .

## See Also

- [Core Animation Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreAnimation_guide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40004514)
- [init(controlPoints: Float, Float, Float, Float)](camediatimingfunction/init(controlpoints:_:_:_:).md)
  Returns an initialized timing function modeled as a cubic Bézier curve using the specified control points.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/camediatimingfunction/init(name:))*