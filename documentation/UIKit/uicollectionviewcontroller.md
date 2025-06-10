# UICollectionViewController

**Framework**: UIKit  
**Kind**: class

A view controller that specializes in managing a collection view.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UICollectionViewController
```

## Mentions

- [Displaying and managing views with a view controller](displaying-and-managing-views-with-a-view-controller.md)

#### Overview

A view controller implements the following behavior:

- If the collection view controller has an assigned nib file or was loaded from a storyboard, it loads its view from the corresponding nib file or storyboard. If you create the collection view controller programmatically, it automatically creates a new unconfigured collection view object, which you can access using the [`collectionView`](uicollectionviewcontroller/collectionview.md) property.
- When loading a collection view from a storyboard or nib file, the data source and delegate objects for the collection view are obtained from the nib file. If a data source or delegate is not specified, the collection view controller assigns itself to the unspecified role.
- When the collection view is about to appear for the first time, the collection view controller reloads the collection view data. It also clears the current selection every time the view is displayed. You can change this behavior by setting the value of the [`clearsSelectionOnViewWillAppear`](uicollectionviewcontroller/clearsselectiononviewwillappear.md) property to [`false`](https://developer.apple.com/documentation/swift/false).

You create a custom subclass of `UICollectionViewController` for each collection view that you want to manage. When you initialize the controller, using the [`init(collectionViewLayout:)`](uicollectionviewcontroller/init(collectionviewlayout:).md) method, you specify the layout the collection view should have. Because the initially created collection view is without dimensions or content, the collection view’s data source and delegate—typically the collection view controller itself—must provide this information.

You may override the [`loadView()`](uiviewcontroller/loadview().md) method or any other superclass method, but if you do, be sure to call `super` in the implementation of your method. If you do not, the collection view controller may not be able to perform all of the tasks needed to maintain the integrity of the collection view.

## Topics

### Creating a collection view controller
- [init(collectionViewLayout: UICollectionViewLayout)](uicollectionviewcontroller/init(collectionviewlayout:).md)
  Initializes a collection view controller and configures the collection view with the provided layout.
- [init(nibName: String?, bundle: Bundle?)](uicollectionviewcontroller/init(nibname:bundle:).md)
  Returns a newly initialized view controller with the nib file in the specified bundle.
- [init?(coder: NSCoder)](uicollectionviewcontroller/init(coder:).md)
  Creates a collection view controller with the nib file in the specified bundle.
### Getting the collection view
- [var collectionView: UICollectionView!](uicollectionviewcontroller/collectionview.md)
  The collection view object managed by this view controller.
- [var collectionViewLayout: UICollectionViewLayout](uicollectionviewcontroller/collectionviewlayout.md)
  The layout object used to initialize the collection view controller.
### Configuring the collection view behavior
- [var clearsSelectionOnViewWillAppear: Bool](uicollectionviewcontroller/clearsselectiononviewwillappear.md)
  A Boolean value indicating if the controller clears the selection when the collection view appears.
- [var installsStandardGestureForInteractiveMovement: Bool](uicollectionviewcontroller/installsstandardgestureforinteractivemovement.md)
  A Boolean value indicating whether the collection view controller installs a standard gesture recognizer to drive the reordering process.
### Integrating with a navigation controller
- [var useLayoutToLayoutNavigationTransitions: Bool](uicollectionviewcontroller/uselayouttolayoutnavigationtransitions.md)
  A Boolean that indicates whether the collection view controller coordinates with a navigation controller for transitions.

## Relationships

### Inherits From
- [UIViewController](uiviewcontroller.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSExtensionRequestHandling](../Foundation/NSExtensionRequestHandling.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSTouchBarProvider](../AppKit/NSTouchBarProvider.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [UIActivityItemsConfigurationProviding](uiactivityitemsconfigurationproviding.md)
- [UIAppearanceContainer](uiappearancecontainer.md)
- [UICollectionViewDataSource](uicollectionviewdatasource.md)
- [UICollectionViewDelegate](uicollectionviewdelegate.md)
- [UIContentContainer](uicontentcontainer.md)
- [UIFocusEnvironment](uifocusenvironment.md)
- [UIPasteConfigurationSupporting](uipasteconfigurationsupporting.md)
- [UIResponderStandardEditActions](uiresponderstandardeditactions.md)
- [UIScrollViewDelegate](uiscrollviewdelegate.md)
- [UIStateRestoring](uistaterestoring.md)
- [UITraitChangeObservable](uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](uitraitenvironment.md)
- [UIUserActivityRestoring](uiuseractivityrestoring.md)

## See Also

- [Displaying and managing views with a view controller](displaying-and-managing-views-with-a-view-controller.md)
  Build a view controller in storyboards, configure it with custom views, and fill those views with your app’s data.
- [Showing and hiding view controllers](showing-and-hiding-view-controllers.md)
  Display view controllers using different techniques, and pass data between them during transitions.
- [class UIViewController](uiviewcontroller.md)
  An object that manages a view hierarchy for your UIKit app.
- [class UITableViewController](uitableviewcontroller.md)
  A view controller that specializes in managing a table view.
- [protocol UIContentContainer](uicontentcontainer.md)
  A set of methods for adapting the contents of your view controllers to size and trait changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewcontroller)*