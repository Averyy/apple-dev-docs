# callAsFunction(value:sharingBehavior:)

**Framework**: SwiftUI  
**Kind**: method

Opens a window defined by a window group that presents the type of the specified value, using the specified sharingBehavior.

**Availability**:
- macOS 15.0+

## Declaration

```swift
@MainActor
func callAsFunction<D>(value: D, sharingBehavior: OpenWindowAction.SharingBehavior) async throws where D : Decodable, D : Encodable, D : Hashable
```

#### Discussion

If sharingBehavior is requested or required, the window is shared if there is an available sharingSession and the person using your app confirms the offer to share. If sharingBehavior is requested and the window is not shared, it is opened normally. If sharingBehavior is required and the window is not shared, it is not opened, and an error is thrown. Regardless of sharingBehavior, an error is thrown if the window fails to open.

Don’t call this method directly. SwiftUI calls it when you call the [`openWindow`](environmentvalues/openwindow.md) action with a value:

```swift
try await openWindow(value: message.id,
sharingBehavior: .requested)
```

For information about how Swift uses the `callAsFunction()` method to simplify call site syntax, see [`Methods with Special Names`](https://developer.apple.comhttps://docs.swift.org/swift-book/ReferenceManual/Declarations.html#ID622) in .

- Parameters - value: The value to present.
- sharingBehavior: the sharing behavior for the opened window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/openwindowaction/callasfunction(value:sharingbehavior:))*