# items

**Framework**: CarPlay  
**Kind**: property

The items to display in the section.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
var items: [CPMapPanelItem] { get set }
```

#### Discussion

You specify the set of items at initialization time, but can change the items at any time. If you change the value of this property while the panel is visible, the system updates your CarPlay interface to reflect the changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmappanelsection/items)*