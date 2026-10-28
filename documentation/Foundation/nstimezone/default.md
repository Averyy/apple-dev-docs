# default

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

The default time zone for the current app.

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
class var `default`: TimeZone { get set }
```

```objc
@property (class, copy) NSTimeZone * defaultTimeZone;
```

## Discussion

If no [`default`](./default.md) time zone has been set, the current system time zone is used. If the current system time zone cannot be determined, the GMT time zone is used instead.

The [`default`](./default.md) time zone is used by the app for date and time operations. You can set it to cause the app to run as if it were in a different time zone. Setting the [`default`](./default.md) property clears any value that was previously set.

If you access the [`default`](./default.md) class property, assign its value to a variable, and set a new [`default`](./default.md) time zone, the object stored in the variable doesn’t update to reflect the new [`default`](./default.md) time zone. Contrast this behavior with that of the [`local`](./local.md) class property, which returns a proxy object that always reflects the current system time zone.

## See Also

### Working with System Time Zones
- [class var local: TimeZone](./local.md)
  An object that tracks the current system time zone.
- [class var system: TimeZone](./system.md)
  The time zone currently used by the system.
- [class func resetSystemTimeZone()](./resetsystemtimezone%28%29.md)
  Clears any time zone value cached for the [`system`](./system.md) property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nstimezone/default)*