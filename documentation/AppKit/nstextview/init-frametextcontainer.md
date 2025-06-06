# init(frame:textContainer:)

**Framework**: AppKit  
**Kind**: init

Initializes a text view.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
init(frame frameRect: NSRect, textContainer container: NSTextContainer?)
```

#### Return Value

An initialized text view.

#### Discussion

This method is the designated initializer for `NSTextView` objects.

Unlike [`init(frame:)`](nstextview/init(frame:).md), which builds up an entire group of text-handling objects, you use this method after you’ve created the other components of the text-handling system — a text storage object, a layout manager, and a text container. Assembling the components in this fashion means that the text storage, not the text view, is the principal owner of the component objects.

The [`init(frame:)`](nstextview/init(frame:).md) initializer uses [`NSLayoutManager`](nslayoutmanager.md) by default. When you use this initializer in macOS 12 and later, you have the option to use [`NSTextLayoutManager`](nstextlayoutmanager.md) which gives you access to newer TextKit functionality and performance improvements. To use the new layout manager  create instances of [`NSTextLayoutManager`](nstextlayoutmanager.md), [`NSTextContainer`](nstextcontainer.md), and [`NSTextContentStorage`](nstextcontentstorage.md); these manage the view’s text layout, text regions, and backingstore, respectively. The example below shows the order of creation and initialization of these objects, and how configure them to initialize an [`NSTextView`](nstextview.md):

```swift
// The viewWidth and viewBounds are set up elsewhere 
// in the App's initialization.

// Create and initialize the supporting layout, container, and storage management.
let textLayoutManager = NSTextLayoutManager()  
let containerSize = NSSize(width: viewWidth, height: CGFloat.greatestFiniteMagnitude)  
let textContainer = NSTextContainer(size: containerSize)  
textLayoutManager.textContainer = textContainer  
let textContentStorage = NSTextContentStorage()  
textContentStorage.addTextLayoutManager(textLayoutManager)  

let textView = NSTextView(frame: viewBounds, textContainer: textLayoutManager.textContainer)

```

In macOS 11 and earlier, you follow a similar pattern but using [`NSLayoutManager`](nslayoutmanager.md) and [`NSTextStorage`](nstextstorage.md) instead:

```swift
// The viewBounds and containerSize are set up elsewhere 
// in the App's initialization.
        
// Create and initialize the supporting layout, container, and storage management.
let textContainer = NSTextContainer(size: containerSize)
let layoutManager = NSLayoutManager()
layoutManager.addTextContainer(textContainer)
let textStorage = NSTextStorage()
textStorage.addLayoutManager(layoutManager)
        
let textView = NSTextView(frame: viewBounds, textContainer: textContainer)

```

## Parameters

- `frameRect`: The frame rectangle of the text view.
- `container`: The text container of the text view.

## See Also

- [Text System User Interface Layer Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/TextUILayer/TextUILayer.html#//apple_ref/doc/uid/10000090i)
- [Cocoa Text Architecture Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/TextFonts/Conceptual/CocoaTextArchitecture/Introduction/Introduction.html#//apple_ref/doc/uid/TP40009459)
- [init(frame: NSRect)](nstextview/init(frame:).md)
  Initializes a text view.
- [convenience init(usingTextLayoutManager: Bool)](nstextview/init(usingtextlayoutmanager:).md)
- [init?(coder: NSCoder)](nstextview/init(coder:).md)
  Initializes a text view with data in an unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/init(frame:textcontainer:))*