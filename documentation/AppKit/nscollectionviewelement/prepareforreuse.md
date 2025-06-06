# prepareForReuse()

**Framework**: AppKit  
**Kind**: method

Performs any necessary cleanup to prepare the element for use again.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@MainActor
optional func prepareForReuse()
```

#### Discussion

The recycling of content is an important technique for improving performance of a collection view. Instead of creating all views from scratch, the collection view recycles views and view controllers that move offscreen. When your app subsequently calls the [`makeItem(withIdentifier:for:)`](nscollectionview/makeitem(withidentifier:for:).md) or [`makeSupplementaryView(ofKind:withIdentifier:for:)`](nscollectionview/makesupplementaryview(ofkind:withidentifier:for:).md) method, the collection view retrieves a recycled object from the appropriate storage, calls this method, and then returns the object to your app.

Implement this method when you need to delete old data or when you want to restore your recycled views to a standard initial state prior to their reuse. For example, you might use this method to restore the size of a view to some standard size or reset the alpha to 1.0 to ensure that the view is fully opaque. Do not use this method to configure the view with new data. Restoring your views to a default state in this method simplifies the configuration code you must write in your data source object later.

If you implement this method, you must call `super` at some point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewelement/prepareforreuse())*