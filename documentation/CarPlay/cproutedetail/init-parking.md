# init(parking:)

**Framework**: CarPlay  
**Kind**: init

Creates additional route information describing parking at the destination.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
convenience init(parking: String)
```

#### Return Value

A new @c CPRouteDetail instance representing the parking information.

#### Discussion

Use this method to surface parking-related details (availability, estimated cost, distance to destination) so users can factor parking into their route selection.

Parking information is displayed alongside other route details. Keep the string concise and localized so it reads clearly in the available space.

## Parameters

- `parking`: A localized string describing parking at the destination. Must not be nil.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cproutedetail/init(parking:))*