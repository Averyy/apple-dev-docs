# HKUserPreferencesDidChange

**Framework**: Foundation  
**Kind**: property

Notifies observers whenever the user changes his or her preferred units.

**Availability**:
- iOS 8.2+
- iPadOS 8.2+
- Mac Catalyst 8.2+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static let HKUserPreferencesDidChange: NSNotification.Name
```

#### Discussion

The preferred units are the units that the user prefers for a given measurement type. By default, the preferred units are based on the device’s current locale. For example, in the US, the preferred units for the [`bodyMass`](https://developer.apple.com/documentation/HealthKit/HKQuantityTypeIdentifier/bodyMass) identifier are pounds. Other regions may use kilograms or stones. However, users can change their preferred units in the Health app at any time.

Each `HKHealthStore` object posts its own `HKUserPreferencesDidChangeNotification` notification. To avoid receiving duplicate notifications, always pass a health store instance to the notification center when adding observers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsnotification/name-swift.struct/hkuserpreferencesdidchange)*