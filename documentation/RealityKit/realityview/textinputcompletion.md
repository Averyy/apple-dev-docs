# textInputCompletion(_:)

**Framework**: RealityKit  
**Kind**: method

Associates a fully formed string with the value of this view when used as a text input suggestion

**Availability**:
- macOS 15.0+

## Declaration

```swift
nonisolated
func textInputCompletion(_ completion: String) -> some View
```

#### Discussion

Use this method to associate a fully formed string with a view that is within a text input suggestion list context. The system uses this value when the view is selected to replace the partial text being currently edited of the associated text field.

```None
TextField("Location", text: $addressText)
    .textInputSuggestions(isEnabled: true) {
        Text("The Fillmore")
            .textInputCompletion("1805 Geary Blvd, San Francisco")
        Text("The Catalyst")
            .textInputCompletion("1011 Pacific Ave, Santa Cruz")
        Text("Rio Theatre")
            .textInputCompletion("1205 Soquel Ave, Santa Cruz")
    }
```

## Parameters

- `text`: A string to use as the view’s completion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/realityview/textinputcompletion(_:))*