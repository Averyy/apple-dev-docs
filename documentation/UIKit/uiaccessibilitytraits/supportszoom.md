# supportsZoom

**Framework**: UIKit  
**Kind**: property

The accessibility element supports zooming in and out on its content.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
nonisolated
static let supportsZoom: UIAccessibilityTraits
```

#### Discussion

Use this trait to characterize an accessibility element that supports zoom functionality, like letting a person perform expand and pinch gestures to zoom in and out. If you assign this trait to an element, you also need to implement [`accessibilityZoomIn(at:)`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class/accessibilityZoomIn(at:)) and [`accessibilityZoomOut(at:)`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class/accessibilityZoomOut(at:)).

For example, the following code shows how to assign this trait to a custom view that allows zooming in to an image:

```swift
class ViewController: UIViewController {
    let zoomView = ZoomingImageView(frame: .zero)
    let imageView = UIImageView(image: UIImage(named: "tree"))

    override func viewDidLoad() {
        super.viewDidLoad()

        zoomView.isAccessibilityElement = true
        zoomView.accessibilityLabel = "Zooming Image View"
        zoomView.accessibilityTraits = [.image, .supportsZoom]

        zoomView.addSubview(imageView)
        view.addSubview(zoomView)
    }
}
```

This custom view implements the required methods to modify the zoom scale and post an announcement about the new zoom scale.

```swift
class ZoomingImageView: UIScrollView {
    override func accessibilityZoomIn(at point: CGPoint) -> Bool {
        zoomScale += 1.0

        let zoomQuantity = "\(Int(zoomScale)) x zoom"
        UIAccessibility.post(notification: .announcement, argument: zoomQuantity)
        return true
    }

    override func accessibilityZoomOut(at point: CGPoint) -> Bool {
        zoomScale -= 1.0

        let zoomQuantity = "\(Int(zoomScale)) x zoom"
        UIAccessibility.post(notification: .announcement, argument: zoomQuantity)
        return true
    }
}
```

> **Note**:  Session 10036: [`Build accessible apps with SwiftUI and UIKit`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2023/10036/)

## See Also

- [static let none: UIAccessibilityTraits](uiaccessibilitytraits/none.md)
  The accessibility element has no traits.
- [static let button: UIAccessibilityTraits](uiaccessibilitytraits/button.md)
  The accessibility element behaves like a button.
- [static let link: UIAccessibilityTraits](uiaccessibilitytraits/link.md)
  The accessibility element behaves like a link.
- [static let image: UIAccessibilityTraits](uiaccessibilitytraits/image.md)
  The accessibility element behaves like an image.
- [static let searchField: UIAccessibilityTraits](uiaccessibilitytraits/searchfield.md)
  The accessibility element behaves like a search field.
- [static let toggleButton: UIAccessibilityTraits](uiaccessibilitytraits/togglebutton.md)
  The accessibility element behaves like a toggle button.
- [static let keyboardKey: UIAccessibilityTraits](uiaccessibilitytraits/keyboardkey.md)
  The accessibility element behaves like a keyboard key.
- [static let staticText: UIAccessibilityTraits](uiaccessibilitytraits/statictext.md)
  The accessibility element behaves like static text that can’t change.
- [static let header: UIAccessibilityTraits](uiaccessibilitytraits/header.md)
  The accessibility element is a header that divides content into sections, such as the title of a navigation bar.
- [static let tabBar: UIAccessibilityTraits](uiaccessibilitytraits/tabbar.md)
  The accessibility element behaves like a tab bar.
- [static let summaryElement: UIAccessibilityTraits](uiaccessibilitytraits/summaryelement.md)
  The accessibility element provides summary information when the app starts.
- [static let selected: UIAccessibilityTraits](uiaccessibilitytraits/selected.md)
  The accessibility element is currently in a selected state.
- [static let notEnabled: UIAccessibilityTraits](uiaccessibilitytraits/notenabled.md)
  The accessibility element isn’t in an enabled state and doesn’t respond to user interaction.
- [static let adjustable: UIAccessibilityTraits](uiaccessibilitytraits/adjustable.md)
  The accessibility element allows continuous adjustment through a range of values.
- [static let allowsDirectInteraction: UIAccessibilityTraits](uiaccessibilitytraits/allowsdirectinteraction.md)
  The accessibility element allows direct touch interaction for VoiceOver users.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccessibilitytraits/supportszoom)*