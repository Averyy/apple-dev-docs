# init(warning:)

**Framework**: CarPlay  
**Kind**: init

Creates additional route information for route warnings.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
convenience init(warning: String)
```

#### Return Value

A new @c CPRouteDetail instance representing a route warning

#### Discussion

Use this method to display important warnings or alerts about conditions along the route. This helps users prepare for challenging or hazardous conditions they may encounter.

Warnings draw attention to significant issues that may affect route safety or accessibility. Use this for critical information that users should be aware of before selecting a route.

> **Note**: Reserve warnings for significant conditions. Use the tintColor property to set an appropriate color (such as red or orange) to ensure warnings are visually prominent. Consider localizing warning messages for international users.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cproutedetail/init(warning:))*