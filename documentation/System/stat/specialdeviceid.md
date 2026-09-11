# specialDeviceID

**Framework**: System  
**Kind**: property

Device ID (if special file)

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
var specialDeviceID: DeviceID { get set }
```

#### Discussion

For character or block special files, the returned `DeviceID` may have meaningful major and minor values. For non-special files, this property is usually meaningless and often set to 0.

The corresponding C property is `st_rdev`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/stat/specialdeviceid)*