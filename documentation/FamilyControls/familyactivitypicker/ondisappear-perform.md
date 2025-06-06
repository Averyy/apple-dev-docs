# onDisappear(perform:)

**Framework**: FamilyControls  
**Kind**: method

Adds an action to perform after this view disappears.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
nonisolated
func onDisappear(perform action: (() -> Void)? = nil) -> some View
```

#### Return Value

A view that triggers `action` after it disappears.

#### Discussion

The exact moment that SwiftUI calls this method depends on the specific view type that you apply it to, but the `action` closure doesn’t execute until the view disappears from the interface.

## Parameters

- `action`: The action to perform. If   is  , the   call has no effect.

## See Also

- [func onAppear(perform: (() -> Void)?) -> some View](familyactivitypicker/onappear(perform:).md)
  Adds an action to perform before this view appears.
- [func onChange<V>(of: V, perform: (V) -> Void) -> some View](familyactivitypicker/onchange(of:perform:).md)
  Performs an action when a specified value changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivitypicker/ondisappear(perform:))*