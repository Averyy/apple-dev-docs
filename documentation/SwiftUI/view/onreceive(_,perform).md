# onReceive(_:perform:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Adds an action to perform when this view detects data emitted by the given publisher.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
nonisolated
func onReceive<P>(_ publisher: P, perform action: @escaping (P.Output) -> Void) -> some View where P : Publisher, P.Failure == Never
```

## Return Value

A view that triggers `action` when `publisher` emits an event.

## Parameters

- `publisher`: The publisher to subscribe to.
- `action`: The action to perform when an event is emitted by `publisher`. The event emitted by publisher is passed as a parameter to `action`.

## See Also

### Responding to data changes
- [func onChange(of:initial:_:)](./onchange%28of,initial,_%29.md)
  Adds a modifier for this view that fires an action when a specific value changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/onreceive(_:perform:))*