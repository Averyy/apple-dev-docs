# monospacedDigit()

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Modifies the text view’s font to use fixed-width digits, while leaving other characters proportionally spaced.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
nonisolated
func monospacedDigit() -> Text
```

## Return Value

A text view with a modified font that uses fixed-width numeric characters, while leaving other characters proportionally spaced.

## Discussion

This modifier only affects numeric characters, and leaves all other characters unchanged.

The following example shows the effect of `monospacedDigit()` on a text view. It arranges two text views in a [`VStack`](../vstack.md), each displaying a formatted date that contains many instances of the character 1. The second text view uses the `monospacedDigit()`. Because 1 is usually a narrow character in proportional fonts, applying the modifier widens all of the 1s, and the text view as a whole. The non-digit characters in the text view remain unaffected.

```swift
let myDate = DateComponents(
    calendar: Calendar(identifier: .gregorian),
    timeZone: TimeZone(identifier: "EST"),
    year: 2011,
    month: 1,
    day: 11,
    hour: 11,
    minute: 11
).date!

var body: some View {
    VStack(alignment: .leading) {
        Text(myDate.formatted(date: .long, time: .complete))
            .font(.system(size: 20))
        Text(myDate.formatted(date: .long, time: .complete))
            .font(.system(size: 20))
            .monospacedDigit()
    }
    .padding()
    .navigationTitle("monospacedDigit() Modifier")
}
```

![Two vertically stacked text views, displaying the date January 11,](https://developer.apple.com/tutorials/images/com.apple.SwiftUI/Text-monospacedDigit-1@2x.png)

If the base font of the text view doesn’t support fixed-width digits, the font remains unchanged.

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
- [func kerning(CGFloat) -> Text](./kerning%28_%29.md)
  Sets the spacing, or kerning, between characters.
- [func tracking(CGFloat) -> Text](./tracking%28_%29.md)
  Sets the tracking for the text.
- [func baselineOffset(CGFloat) -> Text](./baselineoffset%28_%29.md)
  Sets the vertical offset for the text relative to its baseline.
- [Text.Case](./case.md)
  A scheme for transforming the capitalization of characters within text.
- [struct DateStyle](./datestyle.md)
  A predefined style used to display a `Date`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/text/monospaceddigit())*