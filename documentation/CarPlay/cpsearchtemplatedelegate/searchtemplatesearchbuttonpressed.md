# searchTemplateSearchButtonPressed(_:)

**Framework**: CarPlay  
**Kind**: method

Tells the delegate that the user tapped the keyboard’s search button.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
optional func searchTemplateSearchButtonPressed(_ searchTemplate: CPSearchTemplate)
```

#### Discussion

Your implementation of this method should retrieve the search result, and display a [`CPListTemplate`](cplisttemplate.md) containing the search result items by calling [`pushTemplate(_:animated:completion:)`](cpinterfacecontroller/pushtemplate(_:animated:completion:).md).

## Parameters

- `searchTemplate`: The current search template.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpsearchtemplatedelegate/searchtemplatesearchbuttonpressed(_:))*