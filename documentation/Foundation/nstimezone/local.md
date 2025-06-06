# local

**Framework**: Foundation  
**Kind**: property

An object that tracks the current system time zone.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class var local: TimeZone { get }
```

#### Discussion

Use this property when you want an object that always reflects the current system time zone. Contrast this behavior with that of the [`system`](nstimezone/system.md) class property, which has its value cached until you manually clear it by calling the [`resetSystemTimeZone()`](nstimezone/resetsystemtimezone().md) method.

> ❗ **Important**:  In macOS High Sierra and later, iOS 11 and later, tvOS 11 and later, and watchOS 4 and later, the [`local`](nstimezone/local.md) class property reflects the current system time zone, whereas previously it reflected the [`default`](nstimezone/default.md) time zone.

 In macOS High Sierra and later, iOS 11 and later, tvOS 11 and later, and watchOS 4 and later, the [`local`](nstimezone/local.md) class property reflects the current system time zone, whereas previously it reflected the [`default`](nstimezone/default.md) time zone.

Although the time zone obtained here automatically updates with the system, it provides no indication when system settings change. To receive notification of time zone changes, add an observer to the [`NSSystemTimeZoneDidChange`](nsnotification/name-swift.struct/nssystemtimezonedidchange.md) notification by using the [`addObserver(_:selector:name:object:)`](notificationcenter/addobserver(_:selector:name:object:).md).

## See Also

- [class var system: TimeZone](nstimezone/system.md)
  The time zone currently used by the system.
- [class func resetSystemTimeZone()](nstimezone/resetsystemtimezone.md)
  Clears any time zone value cached for the [`system`](nstimezone/system.md) property.
- [class var `default`: TimeZone](nstimezone/default.md)
  The default time zone for the current app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nstimezone/local)*