# system

**Framework**: Foundation  
**Kind**: property

The time zone currently used by the system.

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
class var system: TimeZone { get }
```

#### Discussion

If the current system time zone cannot be determined, the GMT time zone is used instead.

If you access the [`system`](nstimezone/system.md) class property, its value is cached by the app and doesn’t update if the user subsequently changes the system time zone. In order for the [`system`](nstimezone/system.md) property to reflect the new time zone, you must first call the [`resetSystemTimeZone()`](nstimezone/resetsystemtimezone().md) method to clear the cached value. Then, the next time you access the [`system`](nstimezone/system.md) property, it returns the current system time zone, and caches that value.

If you access the [`system`](nstimezone/system.md) class property, assign its value to a variable, and clear the cached value for the property by calling the [`resetSystemTimeZone()`](nstimezone/resetsystemtimezone().md) method, the object stored in the variable doesn’t update to reflect the new system time zone. Contrast this behavior with that of the [`local`](nstimezone/local.md) class property, which returns a proxy object that always reflects the current system time zone.

## See Also

- [class var local: TimeZone](nstimezone/local.md)
  An object that tracks the current system time zone.
- [class func resetSystemTimeZone()](nstimezone/resetsystemtimezone.md)
  Clears any time zone value cached for the [`system`](nstimezone/system.md) property.
- [class var `default`: TimeZone](nstimezone/default.md)
  The default time zone for the current app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nstimezone/system)*