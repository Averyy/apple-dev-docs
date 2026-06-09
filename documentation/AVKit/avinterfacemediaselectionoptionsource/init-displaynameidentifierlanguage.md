# init(displayName:identifier:language:)

**Framework**: AVKit  
**Kind**: init

Creates a new media selection option.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
convenience init(displayName: String, identifier: String, language: Locale.Language? = nil)
```

## Parameters

- `displayName`: Human-readable name displayed in user interfaces.
- `identifier`: Unique system identifier for programmatic selection.
- `language`: The language of the media selection option, or nil for language-neutral content.

## See Also

- [convenience init(displayName: String, identifier: String, extendedLanguageTag: String?)](avinterfacemediaselectionoptionsource/init(displayname:identifier:extendedlanguagetag:).md)
  Creates a new media selection option.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avinterfacemediaselectionoptionsource/init(displayname:identifier:language:))*