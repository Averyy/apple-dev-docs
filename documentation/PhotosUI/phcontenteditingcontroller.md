# PHContentEditingController

**Framework**: PhotosUI  
**Kind**: protocol  
**Role**: Protocol

A protocol your custom view controller class implements to provide a user interface for your Photos extension.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 14.0+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
@MainActor
protocol PHContentEditingController : NSObjectProtocol
```

```objc
@protocol PHContentEditingController <NSObject>
```

## Mentions

- [Creating Photo Editing Extensions](../PhotoKit/creating-photo-editing-extensions.md)

#### Overview

The [`PHContentEditingController`](./phcontenteditingcontroller.md) protocol defines methods you implement in a custom view controller class in order to create a Photos extension. The Photos app hosts your extension’s view controller to provide a user interface for editing photo or video assets.

## Topics

### Working with Adjustment Data
- [func canHandle(PHAdjustmentData) -> Bool](./phcontenteditingcontroller/canhandle%28_%29.md)
  Asks your extension whether it can continue working with the most recent edit that was made to an asset.
### Performing an Edit
- [func startContentEditing(with: PHContentEditingInput, placeholderImage: UIImage)](./phcontenteditingcontroller/startcontentediting%28with,placeholderimage%29.md)
  Tells your extension that asset data is available for editing.
- [func finishContentEditing(completionHandler: (PHContentEditingOutput?) -> Void)](./phcontenteditingcontroller/finishcontentediting%28completionhandler%29.md)
  Asks your extension for edited asset data to finish the editing session.
### Canceling an Edit
- [var shouldShowCancelConfirmation: Bool](./phcontenteditingcontroller/shouldshowcancelconfirmation.md)
  A Boolean value that determines whether Photos should prompt the user when canceling the editing session.
- [func cancelContentEditing()](./phcontenteditingcontroller/cancelcontentediting%28%29.md)
  Tells your extension to cancel editing.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Photo editing extensions
- [Creating Photo Editing Extensions](../PhotoKit/creating-photo-editing-extensions.md)
  Provide custom functionality in the Photos app by bundling an app extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/phcontenteditingcontroller)*