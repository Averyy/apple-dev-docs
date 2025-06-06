# resetFocus

**Framework**: SwiftUI  
**Kind**: property

An action that requests the focus system to reevaluate default focus.

**Availability**:
- macOS 12.0+
- tvOS 14.0+
- watchOS 7.0+

## Declaration

```swift
var resetFocus: ResetFocusAction { get }
```

#### Discussion

Get this environment value and call and call it as a function to force a default focus reevaluation at runtime.

```swift
@Namespace var mainNamespace
@Environment(\.resetFocus) var resetFocus

var body: some View {
    // ...
    resetFocus(in: mainNamespace)
    // ...
}
```

## See Also

- [struct ResetFocusAction](resetfocusaction.md)
  An environment value that provides the ability to reevaluate default focus.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/environmentvalues/resetfocus)*