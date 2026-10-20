# browserAccessibilitySelectedTextRange()

**Framework**: Objective-C Runtime  
**Kind**: method  
**Role**: Instance Method

Returns the range of selected text in the element.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
func browserAccessibilitySelectedTextRange() -> NSRange
```

```objc
- (NSRange) browserAccessibilitySelectedTextRange;
```

#### Return Value

The selection’s range. If there’s no selection, returns `(0,` [`NSNotFound`](../../Foundation/nsnotfound-4qp9h.md)`)`.

## See Also

### Improving browser accessibility
- [func browserAccessibilityAttributedValue(in: NSRange) -> NSAttributedString](./browseraccessibilityattributedvalue%28in%29.md)
  Returns the value for this element within the given range, as an attributed string.
- [func browserAccessibilityDeleteTextAtCursor(numberOfCharacters: Int)](./browseraccessibilitydeletetextatcursor%28numberofcharacters%29.md)
  Deletes text from the element at the current cursor position.
- [func browserAccessibilityInsertTextAtCursor(text: String)](./browseraccessibilityinserttextatcursor%28text%29.md)
  Inserts text into the element at the current cursor position.
- [func browserAccessibilitySetSelectedTextRange(NSRange)](./browseraccessibilitysetselectedtextrange%28_%29.md)
  Updates the element’s selected text.
- [func browserAccessibilityValue(in: NSRange) -> String](./browseraccessibilityvalue%28in%29.md)
  Returns this element’s value in the given range.
- [var browserAccessibilityContainerType: BEAccessibilityContainerType](./browseraccessibilitycontainertype.md)
  The kind of container that contains this element.
- [var browserAccessibilityCurrentStatus: String?](./browseraccessibilitycurrentstatus.md)
  A string that’s the element’s value for aria-current.
- [var browserAccessibilityHasDOMFocus: Bool](./browseraccessibilityhasdomfocus.md)
  A Boolean value that indicates whether the element has native focus in the browser Document Object Model.
- [var browserAccessibilityIsRequired: Bool](./browseraccessibilityisrequired.md)
  A Boolean value that’s the element’s value for aria-required.
- [var browserAccessibilityPressedState: BEAccessibilityPressedState](./browseraccessibilitypressedstate.md)
  The element’s value for aria-pressed.
- [var browserAccessibilityRoleDescription: String?](./browseraccessibilityroledescription.md)
  A string that describes the element’s role for assistive technologies.
- [var browserAccessibilitySortDirection: String?](./browseraccessibilitysortdirection.md)
  A string that’s the element’s value for aria-sort.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/browseraccessibilityselectedtextrange())*