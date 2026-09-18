# showsBottomSeparator

**Framework**: CarPlay  
**Kind**: property

A Boolean value that indicates whether a separator line appears at the bottom edge of the item.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
var showsBottomSeparator: Bool { get set }
```

#### Discussion

When the value of this property is `true`, CarPlay draws a line along the bottom edge of the item to separate it from the next item. Set this property to `false` if you don’t want to draw the separator. The default value of this property is `true`.

When drawing the last section in the map panel, the system doesn’t draw a separator line, even if this property is `true`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cppanelitem/showsbottomseparator)*