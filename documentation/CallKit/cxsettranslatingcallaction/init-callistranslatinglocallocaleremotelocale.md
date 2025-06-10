# init(call:isTranslating:localLocale:remoteLocale:)

**Framework**: CallKit  
**Kind**: init

Initializes a translation action for a call identified by a given UUID, with local and remote locales and a value that indicates whether translation is active.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)

## Declaration

```swift
init(call uuid: UUID, isTranslating: Bool, localLocale: Locale, remoteLocale: Locale)
```

## Parameters

- `uuid`: The unique identifier for the associated   object of the action.
- `isTranslating`: A value that indicates whether translation is active for a call.
- `localLocale`: The local participant’s locale.
- `remoteLocale`: The remote participant’s locale.

## See Also

- [init?(coder: NSCoder)](cxsettranslatingcallaction/init(coder:).md)
  Creates a new action to start or stop translating a call with the provided data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxsettranslatingcallaction/init(call:istranslating:locallocale:remotelocale:))*