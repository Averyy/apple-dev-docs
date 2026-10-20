# x

**Framework**: Core Location  
**Kind**: property  
**Role**: Instance Property

The geomagnetic data (measured in microteslas) for the x-axis.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- watchOS 2.0+

## Declaration

```swift
var x: CLHeadingComponentValue { get }
```

```objc
@property (nonatomic, readonly) CLHeadingComponentValue x;
```

#### Discussion

This value represents the x-axis deviation from the magnetic field lines being tracked by the device.

## See Also

### Getting the raw heading data
- [var y: CLHeadingComponentValue](./y.md)
  The geomagnetic data (measured in microteslas) for the y-axis.
- [var z: CLHeadingComponentValue](./z.md)
  The geomagnetic data (measured in microteslas) for the z-axis.
- [typealias CLHeadingComponentValue](../clheadingcomponentvalue.md)
  A type used to report magnetic differences reported by the onboard hardware.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clheading/x)*