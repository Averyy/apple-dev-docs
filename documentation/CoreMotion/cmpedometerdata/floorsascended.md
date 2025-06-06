# floorsAscended

**Framework**: Core Motion  
**Kind**: property

The approximate number of floors ascended by walking.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- watchOS 2.0+

## Declaration

```swift
var floorsAscended: NSNumber? { get }
```

#### Discussion

This value reflects only the floors ascended while the user was walking or running up stairs and does not reflect the floors ascended by elevator or other assisted means. A single floor has a height of approximately three meters. The value in this property is `nil` when floor counting is not supported on the current device.

## See Also

- [var floorsDescended: NSNumber?](cmpedometerdata/floorsdescended.md)
  The approximate number of floors descended by walking.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmpedometerdata/floorsascended)*