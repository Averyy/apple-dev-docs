# title

**Framework**: AppKit  
**Kind**: property

The localized title of the receiver’s primary view.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
var title: String? { get set }
```

#### Discussion

You can employ the [`title`](nsviewcontroller/title.md) property as needed for your app’s user interface, such as to enable a user to choose among multiple named views in a menu or other affordance. The [`NSViewController`](nsviewcontroller.md) class does not use this property for its own purposes.

The [`title`](nsviewcontroller/title.md) property is key-value coding and key-value observing compliant.

## See Also

- [var view: NSView](nsviewcontroller/view.md)
  The view controller’s primary view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsviewcontroller/title)*