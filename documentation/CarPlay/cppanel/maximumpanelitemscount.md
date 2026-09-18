# maximumPanelItemsCount

**Framework**: CarPlay  
**Kind**: property

The maximum number of items the panel is able to display.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
class var maximumPanelItemsCount: Int { get }
```

#### Discussion

Each panel subtype configures this property with the maximum number of items it’s able to display. When assembling content for your panel, check the value of this property to determine precisely how many items the current type of panel supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cppanel/maximumpanelitemscount)*