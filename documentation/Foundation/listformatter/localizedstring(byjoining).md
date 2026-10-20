# localizedString(byJoining:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Constructs a formatted string from an array of strings that uses the list format specific to the current locale.

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
class func localizedString(byJoining strings: [String]) -> String
```

```objc
+ (NSString *) localizedStringByJoiningStrings:(NSArray<NSString *> *) strings;
```

#### Return Value

A formatted string that joins together a list of strings using a locale-specific list format.

#### Discussion

> 💡 **Tip**:  Use this method to join strings that are ready to be displayed in a bullet-point list. Sentences, phrases with punctuations, and appositions may not work well when joined together.

## Parameters

- `strings`: An array of strings to join together in a list.

## See Also

### Converting Arrays to Formatted Lists
- [func string(from: [Any]) -> String?](./string%28from%29.md)
  Creates a formatted string for an array of items.
- [func string(for: Any?) -> String?](./string%28for%29.md)
  Creates a formatted string for an array of items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/listformatter/localizedstring(byjoining:))*