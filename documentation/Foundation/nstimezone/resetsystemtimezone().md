# resetSystemTimeZone()

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Clears any time zone value cached for the [`system`](./system.md) property.

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

```objc
+ (void) resetSystemTimeZone;
```

#### Discussion

If the app has cached the system time zone by accessing the [`system`](./system.md) class property, this method clears that cached value. If you subsequently access the [`system`](./system.md) class property, a new time zone object is created and cached.

## See Also

### Working with System Time Zones
- [class var local: TimeZone](./local.md)
  An object that tracks the current system time zone.
- [class var system: TimeZone](./system.md)
  The time zone currently used by the system.
- [class var `default`: TimeZone](./default.md)
  The default time zone for the current app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nstimezone/resetsystemtimezone())*