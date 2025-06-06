# NSCollectionViewItem

**Framework**: Appkit  
**Kind**: class

The visual representation for a single data element in a collection view.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
class NSCollectionViewItem
```

#### Overview

Item objects are view controllers, and you use their view hierarchies to display your content. The default implementation of this class supports the creation of a simple item that displays a single image or string. If the appearance or layout of your items is more sophisticated, you can subclass and configure the view hierarchy based on your needs.

Items are the most common types of elements displayed by a collection view, and every collection view must have at least one type of item. You use items to represent the main content of your collection view interface. For example, a photo browser app would use items to display individual photos. Remember that items are only the visual interpretation of your app’s underlying data. The actual data is always managed by your app and exposed to the collection view through the data source object, which uses the data to configure the items that are displayed.

The use of items with a collection view requires doing the following:

- Define the visual appearance of your items by specifying what views they contain and how those views are arranged.
- When your interface is first loaded, register your items with the collection view. (You must register your items before the collection view tries to display any content.)
- In your data source object, create and configure items when the collection view asks for them; see [`NSCollectionViewDataSource`](nscollectionviewdatasource.md).

At runtime, items merely present the data they are given. Your app’s data structures are always the original source of content, and the item contains only a copy of that data to present to the user. When the underlying data associated with an item changes, the data source should invalidate the item by calling the [`reloadItems(at:)`](nscollectionview/reloaditems(at:).md) method of the collection view. Invalidating an item forces the collection view to dispose of it so that the collection view can create a new one with the updated content.

For information about how the collection view displays items to the user, see [`NSCollectionView`](nscollectionview.md).

##### Configuring an Items Views

You configure the views of an item in one of two ways:

- Subclass `NSCollectionViewItem` and create any custom views programmatically.
- Create a nib file containing a single top-level `NSCollectionViewItem` object. Embed any custom views in the root view of the item.

When creating the views programmatically, you typically override the item’s [`loadView()`](nsviewcontroller/loadview().md) method as you would for any view controller. In your implementation, create the views and add them as subviews to the view controller’s root view. Add accessor properties to your subclass so that you can access the views later and configure them.

When using a nib file, you can use a generic `NSCollectionViewItem` object if your item contains only an image or text field. For more complex item content, subclass `NSCollectionViewItem` and add outlets for any views you need to access later. In Interface Builder, connect your outlets to the views you add to the nib file.

##### Registering Items

Before you can ask the collection view to create items, you must register those items using one of the following methods:

- Use the [`register(_:forItemWithIdentifier:)`](nscollectionview/register(_:foritemwithidentifier:)-6s4i.md) method when your `NSCollectionViewItem` subclass handles the creation of its own views.
- Use the [`register(_:forItemWithIdentifier:)`](nscollectionview/register(_:foritemwithidentifier:)-90h1i.md) method when you store the item’s views in a nib file.

> **Note**:  A single collection view can support multiple item types, each with its own distinct appearance, and you can mix and match item types in the same collection view if you want.

You must register at least one item type before trying to display content from your collection view. The collection view’s data source uses the [`makeItem(withIdentifier:for:)`](nscollectionview/makeitem(withidentifier:for:).md) method to fetch an empty item for configuration. During the initial configuration of the collection view, that method creates all items using the registered classes and nib files you provided. Later on, the method may return a recycled item that can be repurposed with new data.

For more information about how how to register items, see [`NSCollectionView`](nscollectionview.md). For information about how the data source object creates and configures items, see [`NSCollectionViewDataSource`](nscollectionviewdatasource.md).

##### Legacy Item Support

For apps built before OS X 10.11, you created a template item and assigned it to the [`itemPrototype`](nscollectionview/itemprototype.md) property of your collection view. To create new instances of the item, you called the collection view’s [`newItem(forRepresentedObject:)`](nscollectionview/newitem(forrepresentedobject:).md) method. For more information about how to support older collection view configurations, see Collection View Programming Guide for macOS.

## Topics

### Getting and Setting Image and Text Fields
- [var imageView: NSImageView?](nscollectionviewitem/imageview.md)
  An image view outlet that you can use to display images.
- [var textField: NSTextField?](nscollectionviewitem/textfield.md)
  A text field outlet that you can use to display a string.
### Managing the Selection and Highlight States
- [var isSelected: Bool](nscollectionviewitem/isselected.md)
  A Boolean indicating whether the item is currently selected.
- [var highlightState: NSCollectionViewItem.HighlightState](nscollectionviewitem/highlightstate-swift.property.md)
  The highlight state currently applied to the item.
### Getting the Parent Collection View
- [var collectionView: NSCollectionView?](nscollectionviewitem/collectionview.md)
  The collection view that owns the item.
### Dragging Components
- [var draggingImageComponents: [NSDraggingImageComponent]](nscollectionviewitem/draggingimagecomponents.md)
  Dragging images for multi-image drag and drop support.
### Constants
- [NSCollectionViewItem.HighlightState](nscollectionviewitem/highlightstate-swift.enum.md)
  Constants indicating the type of highlight applied to an item.

## Relationships

### Inherits From
- [NSViewController](nsviewcontroller.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCollectionViewElement](nscollectionviewelement.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSEditor](nseditor.md)
- [NSExtensionRequestHandling](../Foundation/NSExtensionRequestHandling.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSeguePerforming](nssegueperforming.md)
- [NSStandardKeyBindingResponding](nsstandardkeybindingresponding.md)
- [NSTouchBarProvider](nstouchbarprovider.md)
- [NSUserActivityRestoring](nsuseractivityrestoring.md)
- [NSUserInterfaceItemIdentification](nsuserinterfaceitemidentification.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [protocol NSCollectionViewElement](nscollectionviewelement.md)
  A set of methods that you use to manage the content in a collection view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/AppKit/nscollectionviewitem)*