# focusedValue(_:_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Creates a new view that exposes the provided value to other views whose state depends on the focused view hierarchy.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
nonisolated
func focusedValue<Value>(_ keyPath: WritableKeyPath<FocusedValues, Value?>, _ value: Value?) -> some View
```

**Other overloads**:

```swift
nonisolated
func focusedValue<Value>(_ keyPath: WritableKeyPath<FocusedValues, Value?>, _ value: Value) -> some View
```

## Return Value

A modified representation of this view.

## Discussion

Use this method instead of [`focusedSceneValue(_:_:)`](./focusedscenevalue%28_,_%29.md) when your scene includes multiple focusable views with their own associated values, and you need an app- or scene-scoped element like a command or toolbar item that operates on the value associated with whichever view currently has focus. Each focusable view can supply its own value:

## Parameters

- `keyPath`: The key path to associate `value` with when adding it to the existing table of exported focus values.
- `value`: The focus value to export, or `nil` if no value is currently available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/focusedvalue(_:_:)-odf9)*