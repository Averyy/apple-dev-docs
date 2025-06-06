# Display text with a custom layout

**Framework**: UIKit

Lay out text in a custom-shaped container and apply glyph substitutions.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Xcode 12.0+

#### Overview

Some apps, such as book and magazine readers, text editors, and games, may need to lay out their text in a way that better fits their app style. TextKit provides a set of APIs for these apps to implement a custom text layout. This sample demonstrates how to use the APIs to display text in a circular container and in a two-column container, how to set up an exclusive area for a text container, and how to substitute a glyph without changing the text storage.

##### Implement a Custom Shaped Text Container

When laying out a line of text, TextKit calls the  [`lineFragmentRect(forProposedRect:at:writingDirection:remaining:)`](nstextcontainer/linefragmentrect(forproposedrect:at:writingdirection:remaining:).md) method from [`NSTextContainer`](nstextcontainer.md) to determine the position and size of the line, which TextKit calls a . By creating a subclass of `NSTextContainer` to return a custom line fragment rectangle in the method, apps can implement a custom-shaped text container.

This sample uses the `CircleTextContainer` class to implement a circular text container. To calculate a line fragment rectangle that fits in the inscribed circle of the container’s bounds, the class calls the implementation of `super` to retrieve the default rectangle, then adjusts its `origin.x` and `width` according to the current line origin and container size.

```swift
override func lineFragmentRect(forProposedRect proposedRect: CGRect,
                               at characterIndex: Int,
                               writingDirection baseWritingDirection: NSWritingDirection,
                               remaining remainingRect: UnsafeMutablePointer<CGRect>?) -> CGRect {
    let rect = super.lineFragmentRect(forProposedRect: proposedRect,
                                      at: characterIndex,
                                      writingDirection: baseWritingDirection,
                                      remaining: remainingRect)
    let containerWidth = Float(size.width), containerHeight = Float(size.height)

    let diameter = fminf(containerWidth, containerHeight)
    let radius = diameter / 2.0
    
    // Vertical distance from the line center to the container center.
    let yDistance = fabsf(Float(rect.origin.y + rect.size.height / 2.0) - radius)
    // The new line width.
    let width = (yDistance < radius) ? 2.0 * sqrt(radius * radius - yDistance * yDistance) : 0.0
    // Horizontal distance from rect.origin.x to the starting point of the line.
    let xOffset = (containerWidth > diameter) ? (containerWidth - diameter) / 2.0 : 0.0
    // The starting x of the line.
    let xPosition = CGFloat(xOffset + Float(rect.origin.x) + radius - width / 2.0)
    return CGRect(x: xPosition, y: CGFloat(rect.origin.y), width: CGFloat(width), height: rect.size.height)
}
```

##### Lay Out Text with a Custom Text Container

To lay out text with a custom text container, apps simply set up a text view with the container, and let TextKit do the rest. The  [`init(frame:textContainer:)`](uitextview/init(frame:textcontainer:).md) method from [`UITextView`](uitextview.md) serves this purpose, and this sample uses it to create a `UITextView` instance with its circular text container.

```swift
let textContainer = CircleTextContainer(size: .zero)
textContainer.widthTracksTextView = true

let layoutManager = NSLayoutManager()
layoutManager.addTextContainer(textContainer)
textStorage.addLayoutManager(layoutManager)

textView = UITextView(frame: CGRect.zero, textContainer: textContainer)
```

With this configuration, the TextKit class that coordinates the layout and display of characters,  [`NSLayoutManager`](nslayoutmanager.md), automatically uses the line fragment rectangles that `CircleTextContainer` returns to lay out the text.

`NSLayoutManager` supports laying out text in multiple text containers, so implementing a two-column layout is as easy as adding a second text container to the layout manager, as the code below shows:

```swift
let firstTextContainer = NSTextContainer()
firstTextContainer.widthTracksTextView = true
firstTextContainer.heightTracksTextView = true

let secondTextContainer = NSTextContainer()
secondTextContainer.widthTracksTextView = true
secondTextContainer.heightTracksTextView = true
secondTextContainer.lineBreakMode = .byTruncatingTail

let layoutManager = NSLayoutManager()
layoutManager.addTextContainer(firstTextContainer)
layoutManager.addTextContainer(secondTextContainer)

textStorage.addLayoutManager(layoutManager)

let firstTextView = UITextView(frame: .zero, textContainer: firstTextContainer)
firstTextView.isScrollEnabled = false
view.addSubview(firstTextView)

let secondTextView = UITextView(frame: .zero, textContainer: secondTextContainer)
secondTextView.isScrollEnabled = false
view.addSubview(secondTextView)
```

Note that after adding a second text container to the layout manager, the text views become uneditable and unselectable.

##### Reserve an Area in a Text Container

To create an appealing UI, some apps may have their text wrap around a certain shape. They can achieve that by using the [`exclusionPaths`](nstextcontainer/exclusionpaths.md) property from `NSTextContainer` to reserve an exclusive area for the shape in a text container.

This sample uses the following code to set up an exclusive area where `translatedCirclePath` is a [`UIBezierPath`](uibezierpath.md) instance using the text container’s coordinate system.

```swift
textView.textContainer.exclusionPaths = [translatedCirclePath]
```

##### Substitute Glyphs Without Changing the Text Storage

When a text container doesn’t have enough space to display text, apps may need a way to indicate that the container has additional, or , text. A standard text container can use the  [`lineBreakMode`](nstextcontainer/linebreakmode.md) property from  `NSTextContainer` to add an ending ellipsis that helps handle this situation, but the property doesn’t completely support custom-shaped containers like `CircleTextContainer`.

To show an overflow indicator in its circular text container, as well as to demonstrate TextKit’s capability of glyph substitutions and layout adjustment, this sample substitutes the glyphs of the container’s ending characters with an ellipsis, and makes it the container’s last visible glyph.

The ending characters are the characters of the last words with a total width that is larger than an ellipsis. The characters have to be wider so that the text container has enough space to display the ellipsis. However, because they are wider, the text container has extra space after the glyph substitution, which can drag in more characters. To avoid showing text after the ellipsis, this sample implements a second glyph substitution by selecting the character next to the container’s last word, and substituting it with a control glyph that uses the  [`whitespace`](nslayoutmanager/controlcharacteraction/whitespace.md) action. Using this substitution, the character becomes a whitespace with a width that is flexible. With this flexible space character, the sample can fill up the extra space and push the extra characters to the next line, and then move the line out of the text container.

The detailed implementation of the glyphs substitutions and the layout adjustment is as follows:

- Begin the glyph substitutions by invalidating the glyphs and layout of the ending characters.

```swift
layoutManager.invalidateGlyphs(forCharacterRange: endingWordsCharRange, changeInLength: 0,
                               actualCharacterRange: nil)
layoutManager.invalidateLayout(forCharacterRange: endingWordsCharRange,
                               actualCharacterRange: nil)
```

- Implement the  [`layoutManager(_:shouldGenerateGlyphs:properties:characterIndexes:font:forGlyphRange:)`](nslayoutmanagerdelegate/layoutmanager(_:shouldgenerateglyphs:properties:characterindexes:font:forglyphrange:).md) method from [`NSLayoutManagerDelegate`](nslayoutmanagerdelegate.md) to substitute the glyphs. TextKit calls this delegate method before storing the glyphs to give apps an opportunity to change the glyphs and their properties.

```swift
let ellipsisStartIndex = ellipsisIntersection.location
for index in ellipsisStartIndex..<ellipsisStartIndex + ellipsisIntersection.length {
    if index == ellipsisGlyphRange!.location {
        finalGlyphs[index - glyphRange.location] = myGlyphs[0]
    } else {
        finalProps[index - glyphRange.location] = .controlCharacter
    }
}
let flexibleSpaceStartIndex = flexibleSpaceIntersection.location
for index in  flexibleSpaceStartIndex..<flexibleSpaceStartIndex + flexibleSpaceIntersection.length {
    finalProps[index - glyphRange.location] = .controlCharacter
}
```

- Implement the  [`layoutManager(_:shouldUse:forControlCharacterAt:)`](nslayoutmanagerdelegate/layoutmanager(_:shoulduse:forcontrolcharacterat:).md) method to return the  `NSLayoutManager.ControlCharacterAction.whitespace` action for the flexible space character.

```swift
func layoutManager(_ layoutManager: NSLayoutManager, shouldUse action: NSLayoutManager.ControlCharacterAction,
                   forControlCharacterAt charIndex: Int) -> NSLayoutManager.ControlCharacterAction {
    if let flexibleSpaceGlyphRange = self.flexibleSpaceGlyphRange,
        flexibleSpaceGlyphRange.contains(layoutManager.glyphIndexForCharacter(at: charIndex)) {
        return .whitespace
    }
    return action
}
```

- Implement the  [`layoutManager(_:boundingBoxForControlGlyphAt:for:proposedLineFragment:glyphPosition:characterIndex:)`](nslayoutmanagerdelegate/layoutmanager(_:boundingboxforcontrolglyphat:for:proposedlinefragment:glyphposition:characterindex:).md) method to return a bounding box that can fill up the current line fragment rectangle.

```swift
func layoutManager(_ layoutManager: NSLayoutManager,
                   boundingBoxForControlGlyphAt glyphIndex: Int,
                   for textContainer: NSTextContainer,
                   proposedLineFragment proposedRect: CGRect,
                   glyphPosition: CGPoint,
                   characterIndex charIndex: Int) -> CGRect {
    guard let flexibleSpaceGlyphRange = self.flexibleSpaceGlyphRange,
        flexibleSpaceGlyphRange.contains(glyphIndex) else {
        return CGRect(x: glyphPosition.x, y: glyphPosition.y, width: 0, height: proposedRect.height)
    }
    let padding = textContainer.lineFragmentPadding * 2
    let width = proposedRect.width - (glyphPosition.x - proposedRect.minX) - padding
    let rect = CGRect(x: glyphPosition.x, y: glyphPosition.y, width: width, height: proposedRect.height)
    return rect
}
```

- Implement the  [`layoutManager(_:shouldSetLineFragmentRect:lineFragmentUsedRect:baselineOffset:in:forGlyphRange:)`](nslayoutmanagerdelegate/layoutmanager(_:shouldsetlinefragmentrect:linefragmentusedrect:baselineoffset:in:forglyphrange:).md) method to move the extra line out of the text container.

```swift
func layoutManager(_ layoutManager: NSLayoutManager,
                   shouldSetLineFragmentRect lineFragmentRect: UnsafeMutablePointer<CGRect>,
                   lineFragmentUsedRect: UnsafeMutablePointer<CGRect>,
                   baselineOffset: UnsafeMutablePointer<CGFloat>,
                   in textContainer: NSTextContainer,
                   forGlyphRange glyphRange: NSRange) -> Bool {
    guard let ellipsisGlyphRange = self.ellipsisGlyphRange,
        glyphRange.location > ellipsisGlyphRange.location else {
            return false
    }
    let originX = textContainer.size.width
    lineFragmentRect.pointee.origin = CGPoint(x: originX, y: lineFragmentRect.pointee.origin.y)
    return true
}
```

## See Also

- [Using TextKit 2 to interact with text](using-textkit-2-to-interact-with-text.md)
  Interact with text by managing text selection and inserting custom text elements.
- [class NSTextLayoutManager](nstextlayoutmanager.md)
  The primary class that you use to manage text layout and presentation for custom text displays.
- [class NSTextContainer](nstextcontainer.md)
  A region where text layout occurs.
- [class NSTextLayoutFragment](nstextlayoutfragment.md)
  A class that represents the layout fragment typically corresponding to a rendering surface, such as a layer or view subclass.
- [class NSTextLineFragment](nstextlinefragment.md)
  A class that represents a line fragment as a single textual layout and rendering unit inside a text layout fragment.
- [class NSTextViewportLayoutController](nstextviewportlayoutcontroller.md)
  Manages the layout process inside the viewport interacting with its delegate.
- [protocol NSTextLayoutOrientationProvider](nstextlayoutorientationprovider.md)
  A set of methods that define the orientation of text for an object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/display-text-with-a-custom-layout)*