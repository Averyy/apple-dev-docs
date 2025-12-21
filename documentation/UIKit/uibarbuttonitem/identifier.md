# identifier

**Framework**: UIKit  
**Kind**: property

An identifier used to match bar button items across transitions in a navigation bar or toolbar.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
@MainActor
var identifier: String? { get set }
```

#### Discussion

When the set of bar button items in a navigation bar or toolbar changes (for example, when pushing or popping view controllers), UIKit automatically animates the transition between the different sets of items. By default, UIKit uses heuristics based on item position and content to determine which items should be matched for these transitions.

Set this property with the same value on two different bar button items in different navigation item configurations to indicate that they should be treated as the same item during transitions. This allows for more natural animations when the visuals or function of an item changes across contexts.

The default value is `nil`, which means UIKit will use its default heuristics for transitions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibarbuttonitem/identifier)*