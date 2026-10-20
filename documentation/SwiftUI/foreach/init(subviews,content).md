# init(subviews:content:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates an instance that uniquely identifies and creates views across updates based on the subviews of a given view.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
init<V>(subviews view: V, @ContentBuilder content: @escaping (Subview) -> Content) where Data == ForEachSubviewCollection<Content>, ID == Subview.ID, Content : View, V : View
```

Available when `Data` conforms to `RandomAccessCollection` and `ID` conforms to `Hashable`.

#### Discussion

Subviews are proxies to the resolved view they represent, meaning that modifiers applied to the original view will be applied before modifiers applied to the subview, and the view is resolved using the environment of its container, *not* the environment of the its subview proxy. Additionally, because subviews must represent a single leaf view, or container, a subview may represent a view after the application of styles. As such, attempting to apply a style to it may have no effect.

## Parameters

- `view`: The view to extract the subviews of.
- `content`: The content builder that creates views from subviews.

## See Also

### Creating a collection
- [init(Data)](./init%28_%29.md)
  Creates an instance that uniquely identifies and creates table rows across updates based on the identity of the underlying data.
- [init(_:content:)](./init%28_,content%29.md)
  Creates an instance that uniquely identifies and creates map content across updates based on the identity of the underlying data.
- [init(_:id:content:)](./init%28_,id,content%29.md)
  Creates an instance that uniquely identifies and creates map content across updates based on the provided key path to the underlying data’s identifier.
- [init<V>(sections: V, content: (SectionConfiguration) -> Content)](./init%28sections,content%29.md)
  Creates an instance that uniquely identifies and creates views across updates based on the sections of a given view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/foreach/init(subviews:content:))*