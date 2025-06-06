# CTTextTabGetOptions(_:)

**Framework**: Core Text  
**Kind**: func

Returns the dictionary of attributes associated with the tab.

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
func CTTextTabGetOptions(_ tab: CTTextTab) -> CFDictionary?
```

#### Return Value

The dictionary of attributes associated with the tab, or if no dictionary is present, `NULL`.

## Parameters

- `tab`: The tab whose attributes are obtained.

## See Also

- [func CTTextTabGetAlignment(CTTextTab) -> CTTextAlignment](cttexttabgetalignment(_:).md)
  Returns the text alignment of the tab.
- [func CTTextTabGetLocation(CTTextTab) -> Double](cttexttabgetlocation(_:).md)
  Returns the tab’s ruler location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/cttexttabgetoptions(_:))*