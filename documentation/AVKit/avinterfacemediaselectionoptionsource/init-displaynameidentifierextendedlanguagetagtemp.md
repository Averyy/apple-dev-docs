# init(displayName:identifier:extendedLanguageTagTemp:)

**Framework**: AVKit  
**Kind**: init

Creates a new media selection option.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
convenience init(displayName: String, identifier: String, extendedLanguageTagTemp: Locale.Language? = nil)
```

## Parameters

- `displayName`: Human-readable name displayed in user interfaces.
- `identifier`: Unique system identifier for programmatic selection.
- `extendedLanguageTagTemp`: IETF BCP 47 language identifier, or nil for language-neutral content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avinterfacemediaselectionoptionsource/init(displayname:identifier:extendedlanguagetagtemp:))*