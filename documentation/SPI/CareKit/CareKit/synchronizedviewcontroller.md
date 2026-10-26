---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekit/synchronizedviewcontroller"
framework: "CareKit/CareKit"
---

# SynchronizedViewController

**Framework**: CareKit/CareKit  
**Kind**: class  
**Role**: Class

A view controller that updates a view using a stream of data.

## Declaration

```swift
@MainActor
class SynchronizedViewController<ViewSynchronizer> where ViewSynchronizer : ViewSynchronizing
```

#### Overview

This view controller observes a stream of data from the view it’s mapped to, according to `viewSynchronizer`.

For example,  you want to create a view that is synchronized with a stream of integers. Begin by defining a view synchronizer that creates and updates a `UILabel`:

```swift
final class NumericLabelViewSynchronizer: ViewSynchronizing {

    func makeView() -> UILabel {
        return UILabel()
    }

    func updateView(
        _ view: UILabel,
        context: OCKSynchronizationContext<Int>
    ) {
        view.text = "\(context.viewModel)"
    }
}
```

Next, instantiate a synchronized view controller using the view synchronizer and a stream of integers:

```swift
let viewController = SynchronizedViewController(
    initialViewModel: 0,
    viewModels: [1, 2, 3].async,
    viewSynchronizer: NumericLabelViewSynchronizer()
)
```

The view displays the `initialViewModel` when it’s first instantiated. It then displays each value in the stream of integers.

## Topics

### Initializers
- [init<S>(initialViewModel: ViewSynchronizer.ViewModel, viewModels: S, viewSynchronizer: ViewSynchronizer)](./synchronizedviewcontroller/init%28initialviewmodel,viewmodels,viewsynchronizer%29.md)
  Creates a view controller that updates its view using a stream of data.
### Instance Properties
- [var typedView: ViewSynchronizer.View](./synchronizedviewcontroller/typedview.md)
  The view that the view synchronizer creates.
- [var viewModel: ViewSynchronizer.ViewModel](./synchronizedviewcontroller/viewmodel.md)
  The data displayed in [`typedView`](./synchronizedviewcontroller/typedview.md).
### Instance Methods
- [func viewDidLoad()](./synchronizedviewcontroller/viewdidload%28%29.md)

## Relationships

### Inherits From
- UIKit.UIViewController
### Inherited By
- [OCKCalendarViewController](./ockcalendarviewcontroller.md)
- [OCKChartViewController](./ockchartviewcontroller.md)
- [OCKContactViewController](./ockcontactviewcontroller.md)
- [OCKContactsListViewController](./ockcontactslistviewcontroller.md)
- [OCKTaskViewController](./ocktaskviewcontroller.md)
### Conforms To
- Foundation.NSCoding
- Foundation.NSExtensionRequestHandling
- ObjectiveC.NSObjectProtocol
- Swift.CVarArg
- Swift.CustomDebugStringConvertible
- Swift.CustomStringConvertible
- Swift.Equatable
- Swift.Hashable
- UIKit.UIActivityItemsConfigurationProviding
- UIKit.UIAppearanceContainer
- UIKit.UIContentContainer
- UIKit.UIFocusEnvironment
- UIKit.UIPasteConfigurationSupporting
- UIKit.UIResponderStandardEditActions
- UIKit.UIStateRestoring
- UIKit.UITraitChangeObservable
- UIKit.UITraitEnvironment
- UIKit.UIUserActivityRestoring

## See Also

### Displaying synchronized care data in UIKit
- [protocol ViewSynchronizing](./viewsynchronizing.md)
  A protocol that creates and updates a view.
- [struct OCKSynchronizationContext](./ocksynchronizationcontext.md)
  A data structure that provides context for a view model value.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekit/synchronizedviewcontroller)*