# local

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

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

```objc
@property (class, copy, readonly) NSTimeZone * localTimeZone;
```

#### Discussion

Use this property when you want an object that always reflects the current system time zone. Contrast this behavior with that of the [`system`](./system.md) class property, which has its value cached until you manually clear it by calling the [`resetSystemTimeZone()`](./resetsystemtimezone%28%29.md) method.

> ❗ **Important**:  In macOS High Sierra and later, iOS 11 and later, tvOS 11 and later, and watchOS 4 and later, the [`local`](./local.md) class property reflects the current system time zone, whereas previously it reflected the [`default`](./default.md) time zone.

Although the time zone obtained here automatically updates with the system, it provides no indication when system settings change. To receive notification of time zone changes, add an observer to the [`NSSystemTimeZoneDidChange`](../nsnotification/name-swift.struct/nssystemtimezonedidchange.md) notification by using the [`addObserver(_:selector:name:object:)`](../notificationcenter/addobserver%28_,selector,name,object%29.md).

## See Also

### Working with System Time Zones
- [class var system: TimeZone](./system.md)
  The time zone currently used by the system.
- [class func resetSystemTimeZone()](./resetsystemtimezone%28%29.md)
  Clears any time zone value cached for the [`system`](./system.md) property.
- [class var `default`: TimeZone](./default.md)
  The default time zone for the current app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nstimezone/local)*