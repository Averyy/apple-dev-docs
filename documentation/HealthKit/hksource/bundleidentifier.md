# bundleIdentifier

**Framework**: HealthKit  
**Kind**: property

The source’s bundle identifier.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var bundleIdentifier: String { get }
```

#### Discussion

For apps, this property holds the app’s bundle identifier. For supported Bluetooth LE devices, this property holds a UUID for the device.

## See Also

- [var name: String](hksource/name.md)
  The source’s name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hksource/bundleidentifier)*