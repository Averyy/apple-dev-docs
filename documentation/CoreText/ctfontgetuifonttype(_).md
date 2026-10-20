# CTFontGetUIFontType(_:)

**Framework**: Core Text  
**Kind**: func  
**Role**: Function

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func CTFontGetUIFontType(_ font: CTFont) -> CTFontUIFontType
```

```c
extern CTFontUIFontType CTFontGetUIFontType(CTFontRef font);
```

#### Discussion

Get the CTFontUIFontType of UI font. Note that this value may differ from the uiType parameter originally passed to CTFontCreateUIFontForLanguage, as the system may use a different uiType value internally.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctfontgetuifonttype(_:))*