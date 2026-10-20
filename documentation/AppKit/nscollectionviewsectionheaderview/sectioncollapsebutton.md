# sectionCollapseButton

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A control that lets users collapse and open a collection view section.

**Availability**:
- macOS 10.12+

## Declaration

```swift
@MainActor
@IBOutlet weak optional var sectionCollapseButton: NSButton? { get set }
```

```objc
@property (weak, nullable) NSButton * sectionCollapseButton;
```

#### Discussion

For the best user experience, set this property to the button that lets users control the collapsing of a section so that the collection view can show and hide the button appropriately, based on whether the section’s items can be displayed in the available space. The collection view uses its [`toggleSectionCollapse(_:)`](../nscollectionview/togglesectioncollapse%28_%29.md) property to access this button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewsectionheaderview/sectioncollapsebutton)*