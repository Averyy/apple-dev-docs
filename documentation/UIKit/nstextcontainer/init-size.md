# init(size:)

**Framework**: UIKit  
**Kind**: init

Initializes a text container with a specified bounding rectangle.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
init(size: CGSize)
```

#### Return Value

The size of the text container’s bounding rectangle.

#### Discussion

The new text container must be added to an [`NSLayoutManager`](nslayoutmanager.md) object before it can be used. The text container must also have an associated [`NSTextView`](https://developer.apple.com/documentation/AppKit/NSTextView) object for text to be displayed. This method is the designated initializer for the `NSTextContainer` class.

## Parameters

- `size`: The size of the text container’s bounding rectangle.

## See Also

- [Text Layout Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/TextLayout/TextLayout.html#//apple_ref/doc/uid/10000158i)
- [Cocoa Text Architecture Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/TextFonts/Conceptual/CocoaTextArchitecture/Introduction/Introduction.html#//apple_ref/doc/uid/TP40009459)
- [func addTextContainer(NSTextContainer)](nslayoutmanager/addtextcontainer(_:).md)
  Appends the specified text container to the series of text containers where the layout manager arranges text.
- [Text System Storage Layer Overview](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/TextStorageLayer/TextStorageLayer.html#//apple_ref/doc/uid/10000087i)
- [init(coder: NSCoder)](nstextcontainer/init(coder:).md)
  Creates a text container from data in an unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextcontainer/init(size:))*