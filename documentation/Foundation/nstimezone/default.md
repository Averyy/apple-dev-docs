# default

**Framework**: Foundation  
**Kind**: property

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

#### Discussion

If no [`default`](nstimezone/default.md) time zone has been set, the current system time zone is used. If the current system time zone cannot be determined, the GMT time zone is used instead.

The [`default`](nstimezone/default.md) time zone is used by the app for date and time operations. You can set it to cause the app to run as if it were in a different time zone. Setting the [`default`](nstimezone/default.md) property clears any value that was previously set.

If you access the [`default`](nstimezone/default.md) class property, assign its value to a variable, and set a new [`default`](nstimezone/default.md) time zone, the object stored in the variable doesn’t update to reflect the new [`default`](nstimezone/default.md) time zone. Contrast this behavior with that of the [`local`](nstimezone/local.md) class property, which returns a proxy object that always reflects the current system time zone.

## See Also

- [class var local: TimeZone](nstimezone/local.md)
  An object that tracks the current system time zone.
- [class var system: TimeZone](nstimezone/system.md)
  The time zone currently used by the system.
- [class func resetSystemTimeZone()](nstimezone/resetsystemtimezone.md)
  Clears any time zone value cached for the [`system`](nstimezone/system.md) property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nstimezone/default)*