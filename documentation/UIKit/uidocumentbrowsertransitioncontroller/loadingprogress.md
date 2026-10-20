# loadingProgress

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A progress object that tracks a document as it loads.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var loadingProgress: Progress? { get set }
```

```objc
@property (nonatomic, strong, nullable) NSProgress * loadingProgress;
```

#### Discussion

This property defaults to `nil`. If this property is set, the document browser modifies the document’s thumbnail to show the loading progress.

Use this animation for documents that can take a noticeable amount of time to load.

To set up this animation:

1. Get a transition controller for the document.
2. Set a [`Progress`](../../Foundation/progress.md) object to track the document as it loads. Be sure to keep a strong reference to the transition controller until the animation is complete.
3. Begin loading the document.
4. When the load action is complete, present the document.

The following code provides the loading animation when opening a document.  Note that because [`UIDocument`](../uidocument.md) uses file coordination, the system may delay opening the file until it is available and ready to use. For example, the [`open(completionHandler:)`](../uidocument/open%28completionhandler%29.md) method can trigger the download of a remote file, and the system won’t call the completion handler until the download is complete.

```swift
let doc = // Create a UIDocument subclass for the selected URL.
let editor = // Create a view controller to edit the document.
// Get the transition controller
let transitionController = controller.transitionController(forDocumentURL: url)
// Set the transition controller's progress
transitionController.loadingProgress = doc.loadProgress
// Keep a strong reference to the transition controller
doc.transitionController = transitionController
// Open the document
doc.open { (success) in
    guard success else {
        // Handle the error here...
    }
        
    // When the load is done, present the document
    controller.present(editor, animated: true, completion: nil)
}
```

## See Also

### Animating transitions
- [var targetView: UIView?](./targetview.md)
  The target view for transition animations when presenting or dismissing the transition controller’s document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentbrowsertransitioncontroller/loadingprogress)*