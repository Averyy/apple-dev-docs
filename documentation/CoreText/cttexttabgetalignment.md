# CTTextTabGetAlignment(_:)

**Framework**: Core Text  
**Kind**: func

Returns the text alignment of the tab.

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
func CTTextTabGetAlignment(_ tab: CTTextTab) -> CTTextAlignment
```

#### Return Value

The tab’s text alignment value.

## Parameters

- `tab`: The tab whose text alignment is obtained.

## See Also

- [func CTTextTabGetLocation(CTTextTab) -> Double](cttexttabgetlocation(_:).md)
  Returns the tab’s ruler location.
- [func CTTextTabGetOptions(CTTextTab) -> CFDictionary?](cttexttabgetoptions(_:).md)
  Returns the dictionary of attributes associated with the tab.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/cttexttabgetalignment(_:))*