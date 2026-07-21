# init(info:)

**Framework**: CarPlay  
**Kind**: init

Creates additional route information with a freeform informational string.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
convenience init(info: String)
```

#### Return Value

A new @c CPRouteDetail instance representing the informational text.

#### Discussion

Use this method to display a short piece of general information about the route that does not fit any of the predefined route detail categories.

Info strings should be concise and localized. The system displays this alongside other route details during route selection and active navigation.

## Parameters

- `info`: A localized string containing the information to display. Must not be nil.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cproutedetail/init(info:))*