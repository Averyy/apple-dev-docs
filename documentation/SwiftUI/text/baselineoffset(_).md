# baselineOffset(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Sets the vertical offset for the text relative to its baseline.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
nonisolated
func baselineOffset(_ baselineOffset: CGFloat) -> Text
```

## Return Value

Text that’s above or below its baseline.

## Discussion

Change the baseline offset to move the text in the view (in points) up or down relative to its baseline. The bounds of the view expand to contain the moved text.

```swift
HStack(alignment: .top) {
    Text("Hello")
        .baselineOffset(-10)
        .border(Color.red)
    Text("Hello")
        .border(Color.green)
    Text("Hello")
        .baselineOffset(10)
        .border(Color.blue)
}
.background(Color(white: 0.9))
```

By drawing a border around each text view, you can see how the text moves, and how that affects the view.

![Three text views, each with the word “Hello” outlined by a border and](https://developer.apple.com/tutorials/images/com.apple.SwiftUI/SwiftUI-Text-baselineOffset@2x.png)

The first view, with a negative offset, grows downward to handle the lowered text. The last view, with a positive offset, grows upward. The enclosing [`HStack`](../hstack.md) instance, shown in gray, ensures all the text views remain aligned at their top edge, regardless of the offset.

## Parameters

- `baselineOffset`: The amount to shift the text vertically (up or down) relative to its baseline.

## See Also

### Styling the view’s text
- [func foregroundStyle<S>(S) -> Text](./foregroundstyle%28_%29.md)
  Sets the style of the text displayed by this view.
- [func bold() -> Text](./bold%28%29.md)
  Applies a bold or emphasized treatment to the fonts of the text.
- [func bold(Bool) -> Text](./bold%28_%29.md)
  Applies a bold font weight to the text.
- [func italic() -> Text](./italic%28%29.md)
  Applies italics to the text.
- [func italic(Bool) -> Text](./italic%28_%29.md)
  Applies italics to the text.
- [func strikethrough(Bool, color: Color?) -> Text](./strikethrough%28_,color%29.md)
  Applies a strikethrough to the text.
- [func strikethrough(Bool, pattern: Text.LineStyle.Pattern, color: Color?) -> Text](./strikethrough%28_,pattern,color%29.md)
  Applies a strikethrough to the text.
- [func underline(Bool, color: Color?) -> Text](./underline%28_,color%29.md)
  Applies an underline to the text.
- [func underline(Bool, pattern: Text.LineStyle.Pattern, color: Color?) -> Text](./underline%28_,pattern,color%29.md)
  Applies an underline to the text.
- [func monospaced(Bool) -> Text](./monospaced%28_%29.md)
  Modifies the font of the text to use the fixed-width variant of the current font, if possible.
- [func monospacedDigit() -> Text](./monospaceddigit%28%29.md)
  Modifies the text view’s font to use fixed-width digits, while leaving other characters proportionally spaced.
- [func kerning(CGFloat) -> Text](./kerning%28_%29.md)
  Sets the spacing, or kerning, between characters.
- [func tracking(CGFloat) -> Text](./tracking%28_%29.md)
  Sets the tracking for the text.
- [Text.Case](./case.md)
  A scheme for transforming the capitalization of characters within text.
- [struct DateStyle](./datestyle.md)
  A predefined style used to display a `Date`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/text/baselineoffset(_:))*