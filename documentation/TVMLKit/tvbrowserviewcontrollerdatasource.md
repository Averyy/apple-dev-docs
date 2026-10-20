# TVBrowserViewControllerDataSource

**Framework**: TVMLKit  
**Kind**: protocol  
**Role**: Protocol

Methods adopted by the object you use to represent the browser view.

**Availability**:
- tvOS 13.0+

## Declaration

```swift
protocol TVBrowserViewControllerDataSource : NSObjectProtocol
```

```objc
@protocol TVBrowserViewControllerDataSource <NSObject>
```

#### Overview

Use the data source to provide a document to the browser.

## Topics

### Providing Data
- [func browserViewController(TVBrowserViewController, documentViewControllerFor: TVViewElement) -> TVDocumentViewController?](./tvbrowserviewcontrollerdatasource/browserviewcontroller%28_,documentviewcontrollerfor%29.md)
  Provides the document view controller to be used for a particular child of the full-screen browser.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Providing the Browser’s Data
- [var dataSource: (any TVBrowserViewControllerDataSource)?](./tvbrowserviewcontroller/datasource.md)
  The object that provides data to the full-screen browser.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvbrowserviewcontrollerdatasource)*