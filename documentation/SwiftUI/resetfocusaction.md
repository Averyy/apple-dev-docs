# ResetFocusAction

**Framework**: SwiftUI  
**Kind**: struct

An environment value that provides the ability to reevaluate default focus.

**Availability**:
- macOS 12.0+
- tvOS 14.0+
- watchOS 7.0+

## Declaration

```swift
struct ResetFocusAction
```

#### Overview

Get the [`resetFocus`](environmentvalues/resetfocus.md) environment value and call it as a function to force a default focus reevaluation at runtime.

```swift
@Namespace var mainNamespace
@Environment(\.resetFocus) var resetFocus

var body: some View {
    // ...
    resetFocus(in: mainNamespace)
    // ...
}
```

## Topics

### Calling the action
- [func callAsFunction(in: Namespace.ID)](resetfocusaction/callasfunction(in:).md)
  Asks the focus sytem to reevaluate the default focus item.

## See Also

- [var resetFocus: ResetFocusAction](environmentvalues/resetfocus.md)
  An action that requests the focus system to reevaluate default focus.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/resetfocusaction)*