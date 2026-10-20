# UIPageViewController.OptionsKey

**Framework**: UIKit  
**Kind**: struct  
**Role**: Structure

Keys for creating the page view controller.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
struct OptionsKey
```

```c
typedef NSString * UIPageViewControllerOptionsKey;
```

## Topics

### Page options
- [static let interPageSpacing: UIPageViewController.OptionsKey](./optionskey/interpagespacing.md)
  Space between pages, in points.
- [static let spineLocation: UIPageViewController.OptionsKey](./optionskey/spinelocation.md)
  Location of the spine.
### Initializers
- [init(rawValue: String)](./optionskey/init%28rawvalue%29.md)
  Creates a page view controller options structure with the specified raw value.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Creating a page view controller
- [init(transitionStyle: UIPageViewController.TransitionStyle, navigationOrientation: UIPageViewController.NavigationOrientation, options: [UIPageViewController.OptionsKey : Any]?)](./init%28transitionstyle,navigationorientation,options%29.md)
  Initializes a newly created page view controller.
- [init?(coder: NSCoder)](./init%28coder%29.md)
  Creates a page view controller from data in an unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipageviewcontroller/optionskey)*