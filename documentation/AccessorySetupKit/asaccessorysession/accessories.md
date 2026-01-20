# accessories

**Framework**: AccessorySetupKit  
**Kind**: property

An array of previously-selected accessories for this application.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
var accessories: [ASAccessory] { get }
```

## Mentions

- [Discovering and configuring accessories](discovering-and-configuring-accessories.md)

#### Discussion

To monitor for changes in this list, use your event handler to watch for the events [`ASAccessoryEventType.accessoryAdded`](asaccessoryeventtype/accessoryadded.md), [`ASAccessoryEventType.accessoryChanged`](asaccessoryeventtype/accessorychanged.md), and [`ASAccessoryEventType.accessoryRemoved`](asaccessoryeventtype/accessoryremoved.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorysetupkit/asaccessorysession/accessories)*