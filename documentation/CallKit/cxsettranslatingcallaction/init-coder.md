# init(coder:)

**Framework**: CallKit  
**Kind**: init

Creates a new action to start or stop translating a call with the provided data.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)

## Declaration

```swift
init?(coder aDecoder: NSCoder)
```

## Parameters

- `aDecoder`: An unarchiver object.

## See Also

- [init(call: UUID, isTranslating: Bool, localLocale: Locale, remoteLocale: Locale)](cxsettranslatingcallaction/init(call:istranslating:locallocale:remotelocale:).md)
  Initializes a translation action for a call identified by a given UUID, with local and remote locales and a value that indicates whether translation is active.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxsettranslatingcallaction/init(coder:))*