# language

**Framework**: Background Assets  
**Kind**: property  
**Role**: Instance Property

The language, represented as a BCP-47 identifier, for which this asset pack is localized.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```objc
@property (copy, readonly, nullable) NSString * language;
```

## Discussion

This property is `nil` if the asset pack isn’t localized and therefore isn’t language-specific.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/baassetpack/language)*