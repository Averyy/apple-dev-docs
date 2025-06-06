# viewWillDisappear(_:)

**Framework**: SwiftUI  
**Kind**: method

Notifies the view controller that its view will be removed from a view hierarchy.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency override dynamic func viewWillDisappear(_ animated: Bool)
```

#### Discussion

SwiftUI calls this method before removing the hosting controller’s root view from the view hierarchy. You can override this method to perform custom tasks associated with the disappearance of the view. If you override this method, you must call `super` at some point in your implementation.

## Parameters

- `animated`: If  , the view is being removed   using an animation.

## See Also

- [func loadView()](uihostingcontroller/loadview.md)
- [func viewWillAppear(Bool)](uihostingcontroller/viewwillappear(_:).md)
  Notifies the view controller that its view is about to be added to a view hierarchy.
- [func viewDidAppear(Bool)](uihostingcontroller/viewdidappear(_:).md)
  Notifies the view controller that its view has been added to a view hierarchy.
- [func viewDidDisappear(Bool)](uihostingcontroller/viewdiddisappear(_:).md)
- [func willMove(toParent: UIViewController?)](uihostingcontroller/willmove(toparent:).md)
- [func didMove(toParent: UIViewController?)](uihostingcontroller/didmove(toparent:).md)
- [func viewWillTransition(to: CGSize, with: any UIViewControllerTransitionCoordinator)](uihostingcontroller/viewwilltransition(to:with:).md)
- [func viewWillLayoutSubviews()](uihostingcontroller/viewwilllayoutsubviews.md)
- [func target(forAction: Selector, withSender: Any?) -> Any?](uihostingcontroller/target(foraction:withsender:).md)
- [var rootView: Content](uihostingcontroller/rootview.md)
  The root view of the SwiftUI view hierarchy managed by this view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/uihostingcontroller/viewwilldisappear(_:))*