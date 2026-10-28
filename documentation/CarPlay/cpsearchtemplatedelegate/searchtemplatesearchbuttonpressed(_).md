# searchTemplateSearchButtonPressed(_:)

**Framework**: CarPlay  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the user tapped the keyboard’s search button.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
optional func searchTemplateSearchButtonPressed(_ searchTemplate: CPSearchTemplate)
```

```objc
- (void) searchTemplateSearchButtonPressed:(CPSearchTemplate *) searchTemplate;
```

## Discussion

Your implementation of this method should retrieve the search result, and display a [`CPListTemplate`](../cplisttemplate.md) containing the search result items by calling [`pushTemplate(_:animated:completion:)`](../cpinterfacecontroller/pushtemplate%28_,animated,completion%29.md).

## Parameters

- `searchTemplate`: The current search template.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpsearchtemplatedelegate/searchtemplatesearchbuttonpressed(_:))*