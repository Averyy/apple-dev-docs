# browserAccessibilityAttributedValue(in:)

**Framework**: Objective-C Runtime  
**Kind**: method

Returns the value for this element within the given range, as an attributed string.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS ?+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
func browserAccessibilityAttributedValue(in range: NSRange) -> NSAttributedString
```

#### Return Value

An attributed string that’s the substring of this element’s value within the given range.

## Parameters

- `range`: The range within this element’s value to return.

## See Also

- [func browserAccessibilityDeleteTextAtCursor(numberOfCharacters: Int)](nsobject-swift.class/browseraccessibilitydeletetextatcursor(numberofcharacters:).md)
  Deletes text from the element at the current cursor position.
- [func browserAccessibilityInsertTextAtCursor(text: String)](nsobject-swift.class/browseraccessibilityinserttextatcursor(text:).md)
  Inserts text into the element at the current cursor position.
- [func browserAccessibilitySelectedTextRange() -> NSRange](nsobject-swift.class/browseraccessibilityselectedtextrange.md)
  Returns the range of selected text in the element.
- [func browserAccessibilitySetSelectedTextRange(NSRange)](nsobject-swift.class/browseraccessibilitysetselectedtextrange(_:).md)
  Updates the element’s selected text.
- [func browserAccessibilityValue(in: NSRange) -> String](nsobject-swift.class/browseraccessibilityvalue(in:).md)
  Returns this element’s value in the given range.
- [var browserAccessibilityContainerType: BEAccessibilityContainerType](nsobject-swift.class/browseraccessibilitycontainertype.md)
  The kind of container that contains this element.
- [var browserAccessibilityCurrentStatus: String?](nsobject-swift.class/browseraccessibilitycurrentstatus.md)
  A string that’s the element’s value for aria-current.
- [var browserAccessibilityHasDOMFocus: Bool](nsobject-swift.class/browseraccessibilityhasdomfocus.md)
  A Boolean value that indicates whether the element has native focus in the browser Document Object Model.
- [var browserAccessibilityIsRequired: Bool](nsobject-swift.class/browseraccessibilityisrequired.md)
  A Boolean value that’s the element’s value for aria-required.
- [var browserAccessibilityPressedState: BEAccessibilityPressedState](nsobject-swift.class/browseraccessibilitypressedstate.md)
  The element’s value for aria-pressed.
- [var browserAccessibilityRoleDescription: String?](nsobject-swift.class/browseraccessibilityroledescription.md)
  A string that describes the element’s role for assistive technologies.
- [var browserAccessibilitySortDirection: String?](nsobject-swift.class/browseraccessibilitysortdirection.md)
  A string that’s the element’s value for aria-sort.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/browseraccessibilityattributedvalue(in:))*