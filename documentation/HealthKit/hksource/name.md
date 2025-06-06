# name

**Framework**: HealthKit  
**Kind**: property

The source’s name.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var name: String { get }
```

#### Discussion

For apps, this property holds a localized name for the app. For supported Bluetooth LE devices, this property holds whatever string the device reports as its name.

## See Also

- [var bundleIdentifier: String](hksource/bundleidentifier.md)
  The source’s bundle identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hksource/name)*