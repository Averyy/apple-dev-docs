# initWithDisplayName:identifier:extendedLanguageTag:mediaCharacteristics:

**Framework**: AVKit  
**Kind**: method  
**Role**: Instance Method

Initializes a new media selection option with the specified attributes.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```objc
- (instancetype) initWithDisplayName:(NSString *) displayName identifier:(NSString *) identifier extendedLanguageTag:(NSString *) extendedLanguageTag mediaCharacteristics:(NSArray<NSString *> *) mediaCharacteristics;
```

## Parameters

- `displayName`: Human-readable name displayed in user interfaces.
- `identifier`: Unique system identifier for programmatic selection.
- `extendedLanguageTag`: IETF BCP 47 language identifier, or `nil` for language-neutral content.
- `mediaCharacteristics`: The media characteristics describing accessibility features and content properties of this option.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplaybackuserinterfacemediaselectionoption/initwithdisplayname:identifier:extendedlanguagetag:mediacharacteristics:)*