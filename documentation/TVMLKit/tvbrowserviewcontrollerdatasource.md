# TVBrowserViewControllerDataSource

**Framework**: TVMLKit  
**Kind**: protocol

Methods adopted by the object you use to represent the browser view.

**Availability**:
- tvOS 13.0+

## Declaration

```swift
protocol TVBrowserViewControllerDataSource : NSObjectProtocol
```

#### Overview

Use the data source to provide a document to the browser.

## Topics

### Providing Data
- [func browserViewController(TVBrowserViewController, documentViewControllerFor: TVViewElement) -> TVDocumentViewController?](tvbrowserviewcontrollerdatasource/browserviewcontroller(_:documentviewcontrollerfor:).md)
  Provides the document view controller to be used for a particular child of the full-screen browser.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var dataSource: (any TVBrowserViewControllerDataSource)?](tvbrowserviewcontroller/datasource.md)
  The object that provides data to the full-screen browser.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvbrowserviewcontrollerdatasource)*