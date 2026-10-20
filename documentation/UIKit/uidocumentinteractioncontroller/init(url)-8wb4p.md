# init(url:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Creates a document interaction controller with the specified URL.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
init(url: URL)
```

```objc
+ (UIDocumentInteractionController *) interactionControllerWithURL:(NSURL *) url;
```

#### Return Value

A new document interaction controller object.

## Parameters

- `url`: A URL that specifies the location of the desired document. This parameter is retained. It can be changed later by modifying the [`url`](./url.md) property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentinteractioncontroller/init(url:)-8wb4p)*