# CPSearchTemplateDelegate

**Framework**: CarPlay  
**Kind**: protocol  
**Role**: Protocol

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

```objc
@protocol CPSearchTemplateDelegate <NSObject>
```

## Topics

### Updating the search text
- [func searchTemplate(CPSearchTemplate, updatedSearchText: String, completionHandler: ([CPListItem]) -> Void)](./cpsearchtemplatedelegate/searchtemplate%28_,updatedsearchtext,completionhandler%29.md)
  Tells the delegate that the user updated the search criteria text.
### Selecting a search result
- [func searchTemplate(CPSearchTemplate, selectedResult: CPListItem, completionHandler: () -> Void)](./cpsearchtemplatedelegate/searchtemplate%28_,selectedresult,completionhandler%29.md)
  Tells the delegate that the user selected an item from the search result.
### Handling button presses
- [func searchTemplateSearchButtonPressed(CPSearchTemplate)](./cpsearchtemplatedelegate/searchtemplatesearchbuttonpressed%28_%29.md)
  Tells the delegate that the user tapped the keyboard’s search button.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Managing search behaviors
- [var delegate: (any CPSearchTemplateDelegate)?](./cpsearchtemplate/delegate.md)
  The object that serves as the search template’s delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpsearchtemplatedelegate)*