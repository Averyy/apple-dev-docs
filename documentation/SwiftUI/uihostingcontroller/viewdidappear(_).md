# viewDidAppear(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Notifies the view controller that its view has been added to a view hierarchy.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency override dynamic func viewDidAppear(_ animated: Bool)
```

#### Discussion

SwiftUI calls this method after adding the hosting controller’s root view to the view hierarchy. You can override this method to perform custom tasks associated with the appearance of the view. If you override this method, you must call `super` at some point in your implementation.

## Parameters

- `animated`: If `true`, the view is being added using an animation.

## See Also

### Responding to view-related events
- [func loadView()](./loadview%28%29.md)
- [func viewWillAppear(Bool)](./viewwillappear%28_%29.md)
  Notifies the view controller that its view is about to be added to a view hierarchy.
- [func viewWillDisappear(Bool)](./viewwilldisappear%28_%29.md)
  Notifies the view controller that its view will be removed from a view hierarchy.
- [func viewDidDisappear(Bool)](./viewdiddisappear%28_%29.md)
- [func willMove(toParent: UIViewController?)](./willmove%28toparent%29.md)
- [func didMove(toParent: UIViewController?)](./didmove%28toparent%29.md)
- [func viewWillTransition(to: CGSize, with: any UIViewControllerTransitionCoordinator)](./viewwilltransition%28to,with%29.md)
- [func viewWillLayoutSubviews()](./viewwilllayoutsubviews%28%29.md)
- [func target(forAction: Selector, withSender: Any?) -> Any?](./target%28foraction,withsender%29.md)
- [var rootView: Content](./rootview.md)
  The root view of the SwiftUI view hierarchy managed by this view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/uihostingcontroller/viewdidappear(_:))*