# registerViewElementClass(_:elementName:)

**Framework**: TVMLKit  
**Kind**: method  
**Role**: Type Method

Registers a view element for the specified element name.

**Availability**:
- tvOS 9.0+ - Deprecated in 18.0

> **Deprecated**: Please use SwiftUI or UIKit

## Declaration

```swift
class func registerViewElementClass(_ elementClass: AnyClass, elementName: String)
```

```objc
+ (void) registerViewElementClass:(Class) elementClass forElementName:(NSString *) elementName;
```

## Mentions

- [Creating TVML Elements](../creating-tvml-elements.md)

## Discussion

The [`TVViewElement`](../tvviewelement.md) class represents a read-only DOM node along with its attributes and aggregated style. This model object is traversed by the interface factory to construct views and view controllers, and to render templates. You must call this method for each element you register.

## Parameters

- `elementClass`: The class of the element.
- `elementName`: The element name used when referencing this element within TVML.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvelementfactory/registerviewelementclass(_:elementname:))*