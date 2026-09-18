# sections

**Framework**: CarPlay  
**Kind**: property

The sections of content to display in the panel.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
var sections: [CPMapPanelSection] { get set }
```

#### Discussion

You specify this information initially when you create the panel, but can also update the list of sections by assigning a new value to this property. When assigning a new value to this property, the panel discards the previous data and stores a copy of the new sections you provide.

If the panel isn’t tall enough to display all of the sections at the same time, it places them in a scrollable interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmappanel/sections)*