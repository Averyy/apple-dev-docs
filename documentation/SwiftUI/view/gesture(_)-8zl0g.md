# gesture(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Attaches a [`UIGestureRecognizerRepresentable`](../uigesturerecognizerrepresentable.md) to the view.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+

## Declaration

```swift
nonisolated
func gesture(_ representable: some UIGestureRecognizerRepresentable) -> some View
```

**Other overloads**:

```swift
nonisolated
func gesture(_ representable: some NSGestureRecognizerRepresentable) -> some View
```

## Return Value

A view with a [`UIGestureRecognizerRepresentable`](../uigesturerecognizerrepresentable.md) attached.

## Parameters

- `representable`: The [`UIGestureRecognizerRepresentable`](../uigesturerecognizerrepresentable.md) that creates and manages a gesture recognizer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/gesture(_:)-8zl0g)*