# Slider

**Framework**: SwiftUI  
**Kind**: struct

A control for selecting a value from a bounded linear range of values.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
struct Slider<Label, ValueLabel> where Label : View, ValueLabel : View
```

#### Overview

A slider consists of a “thumb” image that the user moves between two extremes of a linear “track”. The ends of the track represent the minimum and maximum possible values. As the user moves the thumb, the slider updates its bound value.

The following example shows a slider bound to the value `speed`. As the slider updates this value, a bound [`Text`](text.md) view shows the value updating. The `onEditingChanged` closure passed to the slider receives callbacks when the user drags the slider. The example uses this to change the color of the value text.

```swift
@State private var speed = 50.0
@State private var isEditing = false

var body: some View {
    VStack {
        Slider(
            value: $speed,
            in: 0...100,
            onEditingChanged: { editing in
                isEditing = editing
            }
        )
        Text("\(speed)")
            .foregroundColor(isEditing ? .red : .blue)
    }
}
```

![An unlabeled slider, with its thumb about one third of the way from the](https://docs-assets.developer.apple.com/published/9a41fa64a088c04aef5d52935a5b4308/SwiftUI-Slider-simple%402x.png)

You can also use a `step` parameter to provide incremental steps along the path of the slider. For example, if you have a slider with a range of `0` to `100`, and you set the `step` value to `5`, the slider’s increments would be `0`, `5`, `10`, and so on. The following example shows this approach, and also adds optional minimum and maximum value labels.

```swift
@State private var speed = 50.0
@State private var isEditing = false

var body: some View {
    Slider(
        value: $speed,
        in: 0...100,
        step: 5
    ) {
        Text("Speed")
    } minimumValueLabel: {
        Text("0")
    } maximumValueLabel: {
        Text("100")
    } onEditingChanged: { editing in
        isEditing = editing
    }
    Text("\(speed)")
        .foregroundColor(isEditing ? .red : .blue)
}
```

![A slider with labels show minimum and maximum values of 0 and 100,](https://docs-assets.developer.apple.com/published/391df10be6d7d1c252c6d81c8ca0b440/SwiftUI-Slider-withStepAndLabels%402x.png)

The slider also uses the `step` to increase or decrease the value when a VoiceOver user adjusts the slider with voice commands.

## Topics

### Creating a slider
- [init<V>(value: Binding<V>, in: ClosedRange<V>, onEditingChanged: (Bool) -> Void)](slider/init(value:in:oneditingchanged:).md)
  Creates a slider to select a value from a given range.
- [init<V>(value: Binding<V>, in: ClosedRange<V>, step: V.Stride, onEditingChanged: (Bool) -> Void)](slider/init(value:in:step:oneditingchanged:).md)
  Creates a slider to select a value from a given range, subject to a step increment.
### Creating a slider with labels
- [init<V>(value: Binding<V>, in: ClosedRange<V>, label: () -> Label, onEditingChanged: (Bool) -> Void)](slider/init(value:in:label:oneditingchanged:).md)
  Creates a slider to select a value from a given range, which displays the provided label.
- [init<V>(value: Binding<V>, in: ClosedRange<V>, step: V.Stride, label: () -> Label, onEditingChanged: (Bool) -> Void)](slider/init(value:in:step:label:oneditingchanged:).md)
  Creates a slider to select a value from a given range, subject to a step increment, which displays the provided label.
- [init<V>(value: Binding<V>, in: ClosedRange<V>, label: () -> Label, minimumValueLabel: () -> ValueLabel, maximumValueLabel: () -> ValueLabel, onEditingChanged: (Bool) -> Void)](slider/init(value:in:label:minimumvaluelabel:maximumvaluelabel:oneditingchanged:).md)
  Creates a slider to select a value from a given range, which displays the provided labels.
- [init<V>(value: Binding<V>, in: ClosedRange<V>, step: V.Stride, label: () -> Label, minimumValueLabel: () -> ValueLabel, maximumValueLabel: () -> ValueLabel, onEditingChanged: (Bool) -> Void)](slider/init(value:in:step:label:minimumvaluelabel:maximumvaluelabel:oneditingchanged:).md)
  Creates a slider to select a value from a given range, subject to a step increment, which displays the provided labels.
### Deprecated initializers
- [init<V>(value: Binding<V>, in: ClosedRange<V>, onEditingChanged: (Bool) -> Void, label: () -> Label)](slider/init(value:in:oneditingchanged:label:).md)
  Creates a slider to select a value from a given range, which displays the provided label.
- [init<V>(value: Binding<V>, in: ClosedRange<V>, step: V.Stride, onEditingChanged: (Bool) -> Void, label: () -> Label)](slider/init(value:in:step:oneditingchanged:label:).md)
  Creates a slider to select a value from a given range, subject to a step increment, which displays the provided label.
- [init<V>(value: Binding<V>, in: ClosedRange<V>, onEditingChanged: (Bool) -> Void, minimumValueLabel: ValueLabel, maximumValueLabel: ValueLabel, label: () -> Label)](slider/init(value:in:oneditingchanged:minimumvaluelabel:maximumvaluelabel:label:).md)
  Creates a slider to select a value from a given range, which displays the provided labels.
- [init<V>(value: Binding<V>, in: ClosedRange<V>, step: V.Stride, onEditingChanged: (Bool) -> Void, minimumValueLabel: ValueLabel, maximumValueLabel: ValueLabel, label: () -> Label)](slider/init(value:in:step:oneditingchanged:minimumvaluelabel:maximumvaluelabel:label:).md)
  Creates a slider to select a value from a given range, subject to a step increment, which displays the provided labels.

## Relationships

### Conforms To
- [View](view.md)

## See Also

- [struct Stepper](stepper.md)
  A control that performs increment and decrement actions.
- [struct Toggle](toggle.md)
  A control that toggles between on and off states.
- [func toggleStyle<S>(S) -> some View](view/togglestyle(_:).md)
  Sets the style for toggles in a view hierarchy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/slider)*