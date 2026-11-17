# sectionIndexTitle

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

The string that identifies the current session in an index.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var sectionIndexTitle: String? { get }
```

```objc
@property (nonatomic, copy, readonly, nullable) NSString * sectionIndexTitle;
```

## Discussion

For long lists, an index helps people navigate quickly to specific sections of content. This property contains the string you specified at initialization time. If your string contains more than one character, CarPlay displays only the first character in the index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplistsection/sectionindextitle)*