# NSCollectionLayoutEnvironment

**Framework**: AppKit  
**Kind**: protocol

A protocol used to provide information about the layout’s container and environment traits, such as size classes and display scale factor.

**Availability**:
- macOS 10.15+

## Declaration

```swift
@MainActor
protocol NSCollectionLayoutEnvironment : NSObjectProtocol
```

#### Overview

In a section provider, you use the layout environment to get information about the context that the layout appears in. You can get information about the layout’s container, such as its size and content insets, and the traits of its environment, such as size classes, display scale factor, and user interface idiom. You use this information while rendering the layout’s sections to help you make decisions about how to display the layout.

For example, the following code uses the layout environment’s trait collection to check whether the UI is in Dark Mode while creating the layout’s sections.

## Topics

### Getting the layout’s container
- [var container: any NSCollectionLayoutContainer](nscollectionlayoutenvironment/container.md)
  Information about the layout’s container, such as its size and content insets.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionlayoutenvironment)*