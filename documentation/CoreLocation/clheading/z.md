# z

**Framework**: Core Location  
**Kind**: property  
**Role**: Instance Property

The geomagnetic data (measured in microteslas) for the z-axis.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- watchOS 2.0+

## Declaration

```swift
var z: CLHeadingComponentValue { get }
```

```objc
@property (nonatomic, readonly) CLHeadingComponentValue z;
```

#### Discussion

This value represents the z-axis deviation from the magnetic field lines being tracked by the device.

## See Also

### Getting the raw heading data
- [var x: CLHeadingComponentValue](./x.md)
  The geomagnetic data (measured in microteslas) for the x-axis.
- [var y: CLHeadingComponentValue](./y.md)
  The geomagnetic data (measured in microteslas) for the y-axis.
- [typealias CLHeadingComponentValue](../clheadingcomponentvalue.md)
  A type used to report magnetic differences reported by the onboard hardware.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clheading/z)*