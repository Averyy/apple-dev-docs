# init(_:_:)

**Framework**: TipKit  
**Kind**: init

Creates a tip group with the specified presentation priority.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
init(_ priority: TipGroup.Priority = .firstAvailable, @Tips.GroupBuilder _ builder: () -> [any Tip])
```

## Parameters

- `priority`: Presentation priority of the tips. The default value is  .
- `builder`: The tips to display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tipkit/tipgroup/init(_:_:))*