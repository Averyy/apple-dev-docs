# CTTextTabGetLocation(_:)

**Framework**: Core Text  
**Kind**: func

Returns the tab’s ruler location.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func CTTextTabGetLocation(_ tab: CTTextTab) -> Double
```

#### Return Value

The tab’s ruler location relative to the back margin.

## Parameters

- `tab`: The tab whose location is obtained.

## See Also

- [func CTTextTabGetAlignment(CTTextTab) -> CTTextAlignment](cttexttabgetalignment(_:).md)
  Returns the text alignment of the tab.
- [func CTTextTabGetOptions(CTTextTab) -> CFDictionary?](cttexttabgetoptions(_:).md)
  Returns the dictionary of attributes associated with the tab.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/cttexttabgetlocation(_:))*