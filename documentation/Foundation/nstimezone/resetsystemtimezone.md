# resetSystemTimeZone()

**Framework**: Foundation  
**Kind**: method

Clears any time zone value cached for the [`system`](nstimezone/system.md) property.

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
class func resetSystemTimeZone()
```

#### Discussion

If the app has cached the system time zone by accessing the [`system`](nstimezone/system.md) class property, this method clears that cached value. If you subsequently access the [`system`](nstimezone/system.md) class property, a new time zone object is created and cached.

## See Also

- [class var local: TimeZone](nstimezone/local.md)
  An object that tracks the current system time zone.
- [class var system: TimeZone](nstimezone/system.md)
  The time zone currently used by the system.
- [class var `default`: TimeZone](nstimezone/default.md)
  The default time zone for the current app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nstimezone/resetsystemtimezone())*