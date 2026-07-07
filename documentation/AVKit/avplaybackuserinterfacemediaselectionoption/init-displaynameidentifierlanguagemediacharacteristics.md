# init(displayName:identifier:language:mediaCharacteristics:)

**Framework**: AVKit  
**Kind**: init

Creates a new media selection option.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
convenience init(displayName: String, identifier: String, language: Locale.Language? = nil, mediaCharacteristics: [AVMediaCharacteristic] = [])
```

## Parameters

- `displayName`: Human-readable name displayed in user interfaces.
- `identifier`: Unique system identifier for programmatic selection.
- `language`: The language of the media selection option, or `nil` for language-neutral content.
- `mediaCharacteristics`: The media characteristics describing accessibility features and content properties of this option.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplaybackuserinterfacemediaselectionoption/init(displayname:identifier:language:mediacharacteristics:))*