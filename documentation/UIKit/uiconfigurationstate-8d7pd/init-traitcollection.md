# init(traitCollection:)

**Framework**: UIKit  
**Kind**: init  
**Required**: Yes

Creates a view configuration state with the specified trait collection.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- tvOS 14.0+
- visionOS ?+

## Declaration

```swift
init(traitCollection: UITraitCollection)
```

#### Discussion

Typically, you don’t create a configuration state yourself. To obtain a configuration state, override the [`updateConfiguration(using:)`](uicollectionviewcell/updateconfiguration(using:).md) method in your view subclass and use the state parameter. Outside of this method, you can get a view’s configuration state by using its [`configurationState`](uicollectionviewcell/configurationstate-4u37h.md) property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiconfigurationstate-8d7pd/init(traitcollection:))*