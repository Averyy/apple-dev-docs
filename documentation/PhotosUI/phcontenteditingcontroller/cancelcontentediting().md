# cancelContentEditing()

**Framework**: PhotosUI  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Tells your extension to cancel editing.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 14.0+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
func cancelContentEditing()
```

```objc
- (void) cancelContentEditing;
```

#### Discussion

Photos may call this method at any time after your extension view controller’s view appears, including while your app is preparing the editing output.

At this time, your extension should clean up any resources related to your edit and cancel any background work. If the user cancels editing while your app is preparing output, do not call the `completionHandler` block that Photos provided in the [`finishContentEditing(completionHandler:)`](./finishcontentediting%28completionhandler%29.md) method.

## See Also

### Canceling an Edit
- [var shouldShowCancelConfirmation: Bool](./shouldshowcancelconfirmation.md)
  A Boolean value that determines whether Photos should prompt the user when canceling the editing session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/phcontenteditingcontroller/cancelcontentediting())*