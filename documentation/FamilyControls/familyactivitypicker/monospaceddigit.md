# monospacedDigit()

**Framework**: FamilyControls  
**Kind**: method

Modifies the fonts of all child views to use fixed-width digits, if possible, while leaving other characters proportionally spaced.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 12.0+
- tvOS 15.0+
- watchOS 8.0+

## Declaration

```swift
nonisolated
func monospacedDigit() -> some View
```

#### Return Value

A view whose child views’ fonts use fixed-width numeric characters, while leaving other characters proportionally spaced.

#### Discussion

Using fixed-width digits allows you to easily align numbers of the same size in a table-like arrangement. This feature is also known as “tabular figures” or “tabular numbers.”

This modifier only affects numeric characters, and leaves all other characters unchanged.

The following example shows the effect of `monospacedDigit()` on multiple child views. The example consists of two `VStack` views inside an `HStack`. Each `VStack` contains two `Button` views, with the second `VStack` applying the `monospacedDigit()` modifier to its contents. As a result, the digits in the buttons in the trailing `VStack` are the same width, which in turn gives the buttons equal widths.

```swift
var body: some View {
    HStack(alignment: .top) {
        VStack(alignment: .leading) {
            Button("Delete 111 messages") {}
            Button("Delete 222 messages") {}
        }
        VStack(alignment: .leading) {
            Button("Delete 111 messages") {}
            Button("Delete 222 messages") {}
        }
        .monospacedDigit()
    }
    .padding()
    .navigationTitle("monospacedDigit() Child Views")
}
```

If a child view’s base font doesn’t support fixed-width digits, the font remains unchanged.

## See Also

- [func textCase(Text.Case?) -> some View](familyactivitypicker/textcase(_:).md)
  Sets a transform for the case of the text contained in this view when displayed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivitypicker/monospaceddigit())*