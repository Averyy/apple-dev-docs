# init(accessibilityContainer:)

**Framework**: UIKit  
**Kind**: init

Creates and initializes an accessibility element to represent an item in the specified container.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
init(accessibilityContainer container: Any)
```

#### Return Value

An accessibility element to represent a non-view item in the container.

#### Discussion

In general, you do not create accessibility elements for items in your application because standard UIKit controls and views are accessible by default. However, if you have a view that contains nonview items, such as icons or text images, that need to be accessible to users with disabilities, you create accessibility elements to represent them. In this case, the containing view should implement the UIAccessibilityContainer informal protocol and use this method to create an accessibility element to represent each item that should be exposed to an assistive application.

## Parameters

- `container`: The view that contains the accessibility element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccessibilityelement/init(accessibilitycontainer:))*