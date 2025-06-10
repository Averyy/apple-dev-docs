# CPSearchTemplateDelegate

**Framework**: CarPlay  
**Kind**: protocol

The interface for an object that serves as the search template’s delegate.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
protocol CPSearchTemplateDelegate : NSObjectProtocol
```

## Topics

### Updating Search Text
- [func searchTemplate(CPSearchTemplate, updatedSearchText: String, completionHandler: ([CPListItem]) -> Void)](cpsearchtemplatedelegate/searchtemplate(_:updatedsearchtext:completionhandler:).md)
  Tells the delegate that the user updated the search criteria text.
### Selecting a Search Result Item
- [func searchTemplate(CPSearchTemplate, selectedResult: CPListItem, completionHandler: () -> Void)](cpsearchtemplatedelegate/searchtemplate(_:selectedresult:completionhandler:).md)
  Tells the delegate that the user selected an item from the search result.
### Pressing the Search Button
- [func searchTemplateSearchButtonPressed(CPSearchTemplate)](cpsearchtemplatedelegate/searchtemplatesearchbuttonpressed(_:).md)
  Tells the delegate that the user tapped the keyboard’s search button.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var delegate: (any CPSearchTemplateDelegate)?](cpsearchtemplate/delegate.md)
  The object that serves as the search template’s delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpsearchtemplatedelegate)*